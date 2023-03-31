import importlib
from utils.default_values import get_all_models
from utils.logger import log_msg

def load_models():
    models = get_all_models()
    log_msg("INFO", "Loading models : {}".format(models))
    for model in models:
        driverModule = importlib.import_module("drivers.{}".format(model.lower()))
        Driver = getattr(driverModule, "{}Driver".format(model.capitalize()))
        Driver().load_model()
