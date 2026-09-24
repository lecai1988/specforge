from pydantic import BaseModel
from spec import PartSpec
 
 
class BuildResult(BaseModel):
    step_path: str
    stl_path: str
    volume_mm3: float
 
 
def build_part(spec: PartSpec) -> BuildResult:
    import cadquery as cq
 
    # Plate centered at origin: X=length, Y=width, Z=thickness.
    solid = cq.Workplane("XY").box(spec.length, spec.width, spec.thickness)
 
    step_path = f"{spec.name}.step"
    stl_path = f"{spec.name}.stl"
    cq.exporters.export(solid, step_path)
    cq.exporters.export(solid, stl_path)
 
    return BuildResult(
        step_path=step_path,
        stl_path=stl_path,
        volume_mm3=solid.val().Volume(),
    )
