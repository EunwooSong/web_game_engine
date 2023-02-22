from pyodide.ffi import create_proxy, to_js
from js import THREE
from js import document
from js import Object
import asyncio

scene = THREE.Scene.new()

camera1 = THREE.PerspectiveCamera.new(75, 1, 0.1, 10)
camera2 = THREE.OrthographicCamera.new(-1, 1, 1, -1, 0.1, 1000)
camera3 = THREE.OrthographicCamera.new(-1, 1, 1, -1, 0.1, 1000)
camera4 = THREE.OrthographicCamera.new(-1, 1, 1, -1, 0.1, 1000)

camera1.position.z = 2
camera2.position.y = 1
camera2.lookAt(THREE.Vector3.new(0, 0, 0))
camera3.position.x = 1
camera3.lookAt(THREE.Vector3.new(0, 0, 0))
camera4.position.z = 1

renderer1 = THREE.WebGLRenderer.new()
renderer1.setSize(300, 300)
renderer2 = THREE.WebGLRenderer.new()
renderer2.setSize(300, 300)
renderer3 = THREE.WebGLRenderer.new()
renderer3.setSize(300, 300)
renderer4 = THREE.WebGLRenderer.new()
renderer4.setSize(300, 300)

renderer1.domElement.style = ""
renderer2.domElement.style = ""
renderer3.domElement.style = ""
renderer4.domElement.style = ""
document.body.appendChild( renderer1.domElement )
document.body.appendChild( renderer2.domElement )
document.body.appendChild( renderer3.domElement )
document.body.appendChild( renderer4.domElement )

geometry = THREE.BoxGeometry.new()
perms = {"color": "#00ff00", "wireframe": True}
perms = Object.fromEntries(to_js(perms))
material = THREE.MeshBasicMaterial.new(perms)

cube = THREE.Mesh.new(geometry, material)
scene.add(cube)

async def main():
    while True:
        cube.rotation.x += 0.01
        cube.rotation.y += 0.01

        renderer1.render(scene, camera1)
        renderer2.render(scene, camera2)
        renderer3.render(scene, camera3)
        renderer4.render(scene, camera4)
        await asyncio.sleep(0)

asyncio.ensure_future(main())