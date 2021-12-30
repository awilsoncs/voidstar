from components.pathfinding.target_evaluation.target_evaluator import TargetEvaluator
from components.tags.crop_info import CropInfo
from components.target_value import TargetValue


class HighCropTargetEvaluator(TargetEvaluator):
    def get_targets(self, scene):

        return [get_crop_evaluation(scene, tv.entity, tv.value) for tv in scene.cm.get(TargetValue)]


def get_crop_evaluation(scene, entity, value):
    multiplier = 5 if scene.cm.get_one(CropInfo, entity=entity) else 1
    return entity, value*multiplier
