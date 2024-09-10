import torch
from PIL import Image
from torchvision import models, transforms
from pytorch3d.renderer import (
    MeshRenderer,
    MeshRasterizer,
    SoftPhongShader,
    RasterizationSettings,
    OpenGLPerspectiveCameras,
)

def generar_caracteristicas_faciales(image_path):
    facial_model = models.resnet18(pretrained=True)
    facial_model = torch.nn.Sequential(*(list(facial_model.children())[:-1])).cuda()
    facial_model.eval()

    input_image = Image.open(image_path).convert("RGB")
    input_tensor = transforms.ToTensor()(input_image).unsqueeze(0).cuda()
    facial_features = facial_model(input_tensor)
    return facial_features

def renderizar_avatar_3d(mesh, facial_features):
    cameras = OpenGLPerspectiveCameras(device='cuda')
    raster_settings = RasterizationSettings(image_size=256, blur_radius=0.0, faces_per_pixel=1)
    renderer = MeshRenderer(
        rasterizer=MeshRasterizer(cameras=cameras, raster_settings=raster_settings),
        shader=SoftPhongShader(device='cuda')
    )

    images = renderer(meshes_world=mesh, cameras=cameras)
    return images
