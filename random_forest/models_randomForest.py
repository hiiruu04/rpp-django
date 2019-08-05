from django.db import models
from django.utils.text import slugify

from .models_dataset import Dataset as DatasetModel
from .models_setLabel import SetLabel as SetLabelModel
from .models_setFitur import SetFitur as SetFiturModel
from .models_hyperparameterRF import HyperparameterRF as HyperparameterRFModel


def validate_k_cv(value):
    pass


def validate_test_prosentase(value):
    if int(value) <= 5:
        raise ValidationError(
            u'TEST PROSENTASE : input range yang diijinkan 5-50 (%)')


class RandomForest(models.Model):

    default_model = models.BooleanField(default=False)
    dataset = models.ForeignKey(
        DatasetModel, on_delete=models.CASCADE)
    setlabel = models.ForeignKey(
        SetLabelModel, on_delete=models.CASCADE)
    setfitur = models.ForeignKey(
        SetFiturModel, on_delete=models.CASCADE)
    hyperparameter = models.ForeignKey(
        HyperparameterRFModel, on_delete=models.CASCADE)
    test_prosentase = models.IntegerField(default=30,
                                          validators=[validate_test_prosentase])
    rf_result = models.FileField(
        upload_to='randomForest/result/', default='coba.csv')
    rf_fitur_importance = models.FileField(
        upload_to='randomForest/fiturImportance/', default='coba.csv')
    rf_model = models.FileField(
        upload_to='randomForest/model/', default='coba.pkl')

    tanggal_running = models.DateTimeField(auto_now_add=True)

    selected = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.rf_result.delete()
        self.rf_fitur_importance.delete()
        self.rf_model.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return "[{}] 'RF-'{}".format(self.id, str(self.tanggal_running)[1:18])
