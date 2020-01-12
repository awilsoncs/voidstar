class Flux:
    """Data accessor for an entity, which can be applied to a scene."""
    def __init__(self, scene, entity, component, identifier):
        self.scene = scene
        self.entity = entity
        self.component = component
        self.identifier = identifier

    def __call__(self, *args, **kwargs):
        component = self.scene.cm.get_one(self.component, self.entity)
        if component:
            return component.__dict__[self.identifier]
