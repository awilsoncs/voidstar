from systems.animators import animate_float, animate_on_path, animate_delete


def run(scene):
    animate_float.run(scene)
    animate_on_path.run(scene)
    animate_delete.run(scene)
