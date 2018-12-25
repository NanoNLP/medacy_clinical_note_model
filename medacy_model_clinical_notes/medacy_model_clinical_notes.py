from medacy.pipelines import ClinicalPipeline
from medacy.model import Model
from pkg_resources import resource_filename
import os

def load():
    entities = ['Drug', 'Form', 'Route', 'ADE', 'Reason', 'Frequency', 'Duration', 'Dosage', 'Strength']
    pipeline = ClinicalPipeline(entities=entities)
    model = Model(pipeline, n_jobs=1)
    model_directory = resource_filename('medacy_model_clinical_notes', 'model')
    model.load(os.path.join(model_directory, 'n2c2_2018_no_metamap_2018_12_22_16.49.17.pkl'))
    return model

