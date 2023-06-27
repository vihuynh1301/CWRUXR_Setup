import time
import orjson as json
from cwruxr_sdk.common import ToJson, FromJson, Vector3, Pose, Quaternion, Color
from cwruxr_sdk.material_message import MaterialMessage, MRTKMaterialMessage, MRTKStandardParameters

j1 = '{"id":"mat1","shader":"MrtkStandard","color":{"r":255,"g":128,"b":255,"a":128},"renderSettings":{"blending":{"srcBlend":"One","dstBlend":"Zero"},"zWrite":true,"cull":"Back","renderQueue":2000},"parameters":{"metallic":1.0,"smoothness":1.0,"emissiveColor":{"r":255,"g":255,"b":255,"a":255},"rimLightPower":4,"rimLightColor":{"r":255,"g":255,"b":255,"a":255},"texture":{"source":"http://www.google.com","tiling":{"x":1,"y":1},"offset":{"x":0.5,"y":0.5}},"triplanar":false}}'
m1 = MaterialMessage.FromDict(json.loads(j1))

print(m1)
# start_time = time.time()
# m = []
# for i in range(1,100000):
#     m.append(MRTKMaterialMessage(f"m{i}", Color(i,2,3,4), MRTKStandardParameters(1,1,Color(i,2,3,4),4,Color(i,0,0,1),None,False)))
# print(f"Created Material: {time.time()-start_time}")

# start_time = time.time()
# j = ToJson(m)
# #print(j)
# print(f"ToJson: {time.time()-start_time}")

# start_time = time.time()
# m2 = FromJson(j)
# # print(f"FromJson: {time.time()-start_time}")

# # start_time = time.time()
# mats = []
# for mat in m2:
#     mats.append(MaterialMessage.FromDict(mat))
# print(f"To Mat List: {time.time()-start_time}")