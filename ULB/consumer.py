import asyncio
import json
from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync
from channels.consumer import AsyncConsumer
from channels.consumer import SyncConsumer
import json
from ULB.models import ULBdataLabelled, Dataset, Models, ULBdata
from ULB.api.serializers import ULBLabelledSerializers, DatasetSerializers
import random
from channels.db import database_sync_to_async
import pandas as pd
import csv
import pickle
from random_forest.models_randomForest import RandomForest
from django.conf import settings
from django.core.management import call_command

class StreamingConsumer(AsyncConsumer):

    def getAllObj(self):
        if Dataset.objects.filter(finished=0).exists():
            data = Dataset.objects.filter(finished=0)[0]
            filename = settings.MEDIA_ROOT + '/' + str(data.File.name)
            dataset = ULBdata.objects.all()
            dir_file = str(data.File.name)
            return dataset, dir_file
        else:
            dataset = None
            dir_file = None
            return dataset, dir_file

    def labeling(entry):
        if Models.objects.all()[0].is_supervised == 1:
            model = RandomForest.objects.filter(default_model=True)[0]
        else:
            model = RandomForest.objects.filter(default_model=True)[0]
        filename_model = settings.MEDIA_ROOT + '/' + str(model.rf_model)
        rf_model = pickle.load(open(filename_model, 'rb'))
        # entry = entry.drop(["Class"], axis=0)
        Detect = rf_model.predict([[
            entry.Time,
            entry.V1,
            entry.V2,
            entry.V3,
            entry.V4,
            entry.V5,
            entry.V6,
            entry.V7,
            entry.V8,
            entry.V9,
            entry.V10,
            entry.V11,
            entry.V12,
            entry.V13,
            entry.V14,
            entry.V15,
            entry.V16,
            entry.V17,
            entry.V18,
            entry.V19,
            entry.V20,
            entry.V21,
            entry.V22,
            entry.V23,
            entry.V24,
            entry.V25,
            entry.V26,
            entry.V27,
            entry.V28,
            entry.Amount],])
        new_data = ULBdataLabelled(
            Time = entry.Time,
            V1 = entry.V1,
            V2 = entry.V2,
            V3 = entry.V3,
            V4 = entry.V4,
            V5 = entry.V5,
            V6 = entry.V6,
            V7 = entry.V7,
            V8 = entry.V8,
            V9 = entry.V9,
            V10 = entry.V10,
            V11 = entry.V11,
            V12 = entry.V12,
            V13 = entry.V13,
            V14 = entry.V14,
            V15 = entry.V15,
            V16 = entry.V16,
            V17 = entry.V17,
            V18 = entry.V18,
            V19 = entry.V19,
            V20 = entry.V20,
            V21 = entry.V21,
            V22 = entry.V22,
            V23 = entry.V23,
            V24 = entry.V24,
            V25 = entry.V25,
            V26 = entry.V26,
            V27 = entry.V27,
            V28 = entry.V28,
            Amount = entry.Amount,
            Detect = Detect[0],
        )
        new_data.save()
        return new_data

    async def label_data(self, dataset_entries, file_dir):
        if dataset_entries is not None:
            for entry in dataset_entries:
                await asyncio.sleep(0.001)
                new_data = StreamingConsumer.labeling(entry)
                serialized = ULBLabelledSerializers(new_data)
                await self.send({
                    "type": "websocket.send",
                    "text": json.dumps(serialized.data),
                })
            data = Dataset.objects.get(File=file_dir)
            data.finished = 1
            data.save()
        else:
            await self.send({
                "type": "websocket.send",
                "text": "Data Habis, silahkan upload data untuk diprediksi terlebih dahulu",
            })
            await asyncio.sleep(30)

    async def reconnect_delay(self, delay):
        await asyncio.sleep(delay)
        await self.send({
                "type":"websocket.close",
        })

    async def websocket_connect(self, event):
        print("connected", event)
        
        await self.send({
            "type": "websocket.accept",
        })
        data_entries, file_dir = await database_sync_to_async(self.getAllObj)()

        await self.label_data(data_entries, file_dir)

        await self.reconnect_delay(10)


    async def websocket_receive(self, event):
        print("receive", event)

    async def websocket_disconnect(self, event):
        print("disconnect", event)