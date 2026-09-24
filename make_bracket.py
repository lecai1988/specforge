from spec import PartSpec
from geometry import build_part
 
spec = PartSpec(name="hello-bracket", length=80.0, width=50.0, thickness=6.0)
result = build_part(spec)
 
print("STEP file:", result.step_path)
print("STL file: ", result.stl_path)
print("Volume:   ", result.volume_mm3, "mm^3")
print("Expected: ", 80.0 * 50.0 * 6.0, "mm^3")
