import unittest
from dataclasses import dataclass

from engine.base_components.component import Component
from engine.component_manager import ComponentManager


class TestComponentManager(unittest.TestCase):
    def test_instantiation(self):
        ComponentManager()

    def test_add_retrieve_component(self):
        @dataclass
        class FakeComponent(Component):
            pass

        cm = ComponentManager()
        fc = FakeComponent(id=1, entity=2)

        cm.add(fc)
        fcs = cm.get(FakeComponent)

        self.assertIn(fc, fcs)
        self.assertEqual(1, len(fcs))

    def test_add_retrieve_by_supertype(self):
        @dataclass
        class FakeComponent(Component):
            pass

        cm = ComponentManager()
        fc = FakeComponent(id=1, entity=2)
        cm.add(fc)
        cs = cm.get(Component)

        self.assertIn(fc, cs)
        self.assertEqual(1, len(cs))

    def test_get_one_by_supertype(self):
        @dataclass
        class FakeComponent(Component):
            pass

        cm = ComponentManager()
        fc = FakeComponent(id=1, entity=2)
        cm.add(fc)
        cs = cm.get_one(Component, entity=2)

        self.assertEqual(fc, cs)

    def test_delete_component(self):
        @dataclass
        class FakeComponent(Component):
            pass

        cm = ComponentManager()
        fc = FakeComponent(id=1, entity=2)
        cm.add(fc)

        cm.delete_component(fc)
        cs = cm.get_one(Component, entity=2)

        self.assertIsNone(cs)

    def test_delete_entity(self):
        @dataclass
        class A(Component):
            pass

        @dataclass
        class B(Component):
            pass

        cm = ComponentManager()
        cm.add(A(entity=2))
        cm.add(B(entity=2))
        cm.delete(2)

        fs_a = cm.get_one(A, entity=2)
        self.assertIsNone(fs_a, "component manager contains base_components that should be orphaned")

        fs_b = cm.get_one(B, entity=2)
        self.assertIsNone(fs_b, "component manager contains base_components that should be orphaned")


if __name__ == '__main__':
    unittest.main()
