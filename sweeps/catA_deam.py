from sweeps import makeSweepTrainer
from models import ModelCatA

CMDS = ModelCatA.CMDS

DEFAULT_DATA_ARTIFACT = "deam:latest"
DEFAULT_SPLIT_ARTIFACT = "deam-train-70-val-20-test-10-seed-42:latest"
DEFAULT_CONFIG = dict(map(lambda x: (x[0], x[2]), CMDS))

makeTrainer = makeSweepTrainer(ModelCatA, monitor='val/acc')

def get_parse_args():
    return (DEFAULT_DATA_ARTIFACT, DEFAULT_SPLIT_ARTIFACT, CMDS)
