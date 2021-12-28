from components.pathfinding.target_evaluation.target_evaluator import TargetEvaluator
from components.target_value import TargetValue


class HordelingTargetEvaluator(TargetEvaluator):
    def get_targets(self, scene):
        return [(tv.entity, tv.value) for tv in scene.cm.get(TargetValue)]
