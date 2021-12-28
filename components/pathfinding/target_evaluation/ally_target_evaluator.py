from components.pathfinding.target_evaluation.target_evaluator import TargetEvaluator
from components.tags.hordeling_tag import HordelingTag


class AllyTargetEvaluator(TargetEvaluator):
    def get_targets(self, scene):
        return [(tv.entity, 1) for tv in scene.cm.get(HordelingTag)]
