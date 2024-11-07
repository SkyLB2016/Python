# -*- coding: utf-8 -*-
"""
@Time    : 2024/11/7 11:31
@Author  : sky
@Email   : your-email@example.com
@File    : down_file.py
@Description: 
"""
import os

import requests
from urllib.parse import urlparse

from application import tools


def get_task_id():
    api_key = os.environ.get("DASHSCOPE_API_KEY")
    # print(api_key)

    # 1.定义URL
    url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis'
    # 2.定义请求头，常见的头部包括 `Content-Type` 和 `Authorization`。
    headers = {
        "Sec-Fetch-Dest": "image",
        'X-DashScope-Async': 'enable',
        'Content-Type': 'application/json',
        # 'Authorization': 'Bearer sk-57134a934d3d4d2d99d84d2812f88424'
        'Authorization': f'Bearer {api_key}'
    }
    # 3.定义POST请求参数
    data = {
        "model": "wanx-v1",
        # "model": "FindAgent",
        "input": {
            # "prompt": "中国美少女，长腿内衣，翘臀，高分辨率，增加细节，细节强化，正面视角，肤若凝脂，面如冠玉，极高分辨率，清晰度强化，山水间"
            "prompt": "中国美少女，长腿内衣，坐姿，叉开腿，高分辨率，增加细节，细节强化，正面视角，肤若凝脂，面如冠玉，精致的脸部比例，极高分辨率，清晰度强化，室内"
        },
        "parameters": {
            "style": "<auto>",
            # "size": "720*1280",
            "size": "1080*1080",
            "n": 1
        }
    }
    # 4.发送POST请求，并传递 URL、头部和数据。
    response = requests.post(url, headers=headers, json=data)
    # 5.检查响应状态码
    if response.status_code == 200:
        # 6.打印响应内容
        # print(response.json())
        content = response.json()
        task_id = content['output']['task_id']
        # print(task_id)
        return task_id
    else:
        # 打印响应内容
        print(f'请求失败，状态码: {response.status_code}')
        # print(f'请求失败，状态码: {response.status_code}', response.text)


def get_image_url(task_id):
    # 1.定义URL
    # url_template = 'https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}'
    # url = url_template.format(task_id=task_id)
    url = f'https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}'
    # 2.定义请求头，常见的头部包括 `Content-Type` 和 `Authorization`。
    headers = {
        'X-DashScope-Async': 'enable',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer sk-57134a934d3d4d2d99d84d2812f88424'
    }
    # 3.定义 GET 请求参数
    # params = {
    #     'task_id': task_id
    # }
    # 4.发送POST请求，并传递 URL、头部和数据。
    # response = requests.get(url, headers=headers,params=params)
    response = requests.get(url, headers=headers)
    # 5.检查响应状态码
    if response.status_code == 200:
        # 6.打印响应内容
        # print(response.json())
        content = response.json()
        output = content['output']
        if 'results' in output:
            url = output['results'][0]['url']
            print("url", url)
            return url
        else:
            print(output)
        return None
    else:
        # 打印响应内容
        print(f'请求失败，状态码: {response.status_code}', response.text)


# 下载文件
def dowmload_image(image_url, dir=''):
    # 目标 URL
    # 解析 URL 以提取文件名
    parsed_url = urlparse(image_url)
    path = parsed_url.path
    file_name = path.split('/')[-1]
    # 如果文件名中包含查询参数，去除查询参数部分
    if '?' in file_name:
        file_name = file_name.split('?')[0]

    # 定义保存文件的路径
    file_path = "../../static/ty_images/" + dir + "/"
    tools.check_path(file_path)
    file_path = file_path + file_name
    # 发送 GET 请求
    response = requests.get(image_url)

    # 检查请求是否成功
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f'文件已成功下载并保存为 {file_path}')
    else:
        print(f'请求失败，状态码: {response.status_code}')
        print('响应内容:', response.text)


task_ids = []
for i in range(0, 32):
    id = get_task_id()
    if id:
        task_ids.append(id)
print(task_ids)
print(len(task_ids))
task_ids = ['ebce4c06-4d56-4700-8030-f2433bf5704b', '383c289f-ca2f-4fb0-a80b-f19e210ac599', '5556f9d5-6c0b-4186-96a8-77b00271fe12', '08e51734-d0e9-40af-83f9-1fd4b47a4e4d', 'f58b69f5-aa00-4204-bb97-914e28cbbb5d', '48c8040c-bdbd-4042-a6db-8b08206c44e1', '1ec4dbb2-904e-42bf-89d7-47a651feef23', '65f9fdb6-6aee-4686-a89e-6cb5d609a565', '380971fa-e447-4d57-b6c1-dcc7bc4bc2b3', '8fad3fdc-1f70-4a81-914a-a5abfc043aaf', 'e3b39eda-dc28-4406-8455-30639e7d1053', '06756f4a-ac79-4453-862a-fb91d38b3d4a', '387b67bf-34b5-4f1f-aae6-22ef6637da6f', 'b104e85a-e484-4ce5-b22f-25ae62401b96', 'f88a464a-aec1-441f-ba21-365e7cc7a6fc', '649d7ebb-51a0-4fe1-8a54-e0047ea0d8f1', 'b6607914-fe51-4203-86ad-074cecd5377f', 'edc69fd6-14fa-49a7-8787-c74cdac8c3f7', 'd2e6d9c3-5116-4cb4-806d-aa5dad045df7', '36c67761-3f76-4bb6-9eba-9dcd32e81e4d', '9cb79aab-b9c2-4bc0-ab56-3879ed2b0e69', 'c111165e-a0d4-4b8b-9322-eeb06f85dbc8', '460545d8-5b64-41bd-8282-dca11e29f0cf', '042ca8f9-17af-4e1b-999e-b6f91dd8f269', '8b628a8c-84ae-4000-8623-0abe561d4d89', '1b278b08-988d-4a21-a023-f66c0bc0c222', '70f43323-92e7-4d41-aeef-c49e94df8713', '5cee3bdf-1917-4bf3-a51e-e89dffc65ab0', 'eea4532a-f187-4e52-9ae4-8875d4022238', '1c252729-124c-416f-a109-f29184e66b4d', 'a017cd4b-3016-453c-a4be-a89f277e637e', 'd50d252e-ab72-4cf5-86ee-cdc8af49c8b1', 'a281ca7d-dc41-41a0-a1e3-a6342aa94a73', '4eafc151-d98e-4842-aa0c-97a9d693df02', '104562a4-5bc7-40ce-a5db-37fc5581ac07', 'f2a6d402-9a49-4a2a-b275-6eda6923b375', '49746a53-b35d-41ae-b517-2140ef138e77', '510d059a-eb50-436a-b57f-c37b8e344acf', 'c25e47ab-a49e-43fb-9079-aa5662a6d24f', '8aaa522d-ed89-4b32-aa20-e48806ed4d6f', '5004238c-7dbd-42a2-9afb-209799c47757', 'e040a535-60c0-4cb5-9548-0e8f538aefd3', '45d12a64-4e22-4f53-9386-29d6f1626dea', 'd01b69d0-a5c4-49db-8b81-4a2401f22d48', '709ff025-e384-41f8-833b-37ebcfaeb43a', '3acab0f1-f418-4293-90e4-05b30eeebbc2', '32bc2888-a993-4fc6-aa97-2a03e3ffb01f', 'cb15dce4-2a12-43f9-b3d2-664a50d11122', 'b3b9f272-8dc6-4aa2-aae2-d6afaa85f2a2', '6de2c6c7-e147-4f2b-8439-24eb7371bd90', 'b4051532-7804-4680-842c-119f102a7f16', '80dca606-5f6f-464b-8a05-a2b55932d67c', '5a854c4e-cbae-4a23-b7c6-d609e7f3305a', '17b6a8c1-cd60-47af-b9e5-92d32ba4c984', '6d265c53-ff89-4e63-96e5-de419ceda627', '0e569b32-c114-4e02-97d1-238e3ee3eb21', 'f3b407b5-4db5-4f59-835b-a41d837feede', 'e3ad5546-0f39-4d22-90c4-73814633ba25', '71b717e8-e206-43f8-bfe3-aa904db36aab', '2ceb1c8f-02e1-4e59-9ca4-52a38d9336d7', 'aeebaada-e55c-447b-89d4-46e09d147d6e', '6aacf0dd-788b-4f8a-9b3c-23ee64d94f2a', '6f4042ec-1a49-4240-8f55-9d7df44793e5', '168bd0d8-c144-4a95-805c-6fe8729357ed', 'aaabdec1-e8ce-4954-a2a6-57e8f8daef48', 'd48b30c6-e403-409f-b733-a57c10493150', 'f98f6b34-e33f-4f29-bf69-74b20bce7afe', '7e6f88d9-068a-4db6-b232-7a50a2b4792f', 'c2da3f5f-c2a1-42b5-b0b6-7b6d072ea06a', '82c2dde4-4382-4a0a-ba70-4f78184b61dc', '59a3f360-2317-461d-b13f-83837c0a3a56', '624519a4-7db3-47f1-8acf-e04ba33f4bed', '60a3aa3a-5c1e-4885-8183-05bd7c9a0f48', '0a38039f-21e2-49d0-b562-144f895ff99e', '7cac6aad-17b4-4969-9993-6c6139ad5a1d', '0ebe6b1d-03ff-4164-a175-d8a0d85dbe5c', 'ab8e96e1-fb81-42cb-a540-122ec224b2cb', '13718803-3e6b-400e-a880-ba8127deb660', '0bc5796b-fd94-4c97-adf4-24204a612e4d', 'c997f0ce-d970-430c-9f1e-be7925a0a824', '04febea8-6f83-4a6d-9c0e-cd6bb66eb196', '1e854c5f-4482-4990-9599-efd83b836293', '36b2b45b-c552-4bec-ab0b-331d57e68ecb', 'f7c1e943-727d-4527-8bb3-c86761f02ef8', '81bbc0bd-e171-433b-8753-8c1b84367d02', 'e1ab9de4-7367-494a-91ed-1e43464b4b31', '57a1133e-9773-4613-98b2-17d04a4888b3', '6ba136e6-d68e-4dae-b738-ebe40964b3d5', '3907125b-9981-494d-b6b9-76f6dac11763', '843ee077-ffe3-4388-89ea-ca9bf32fd71d', '7822ce85-044d-4467-b54d-a2a345b7cf91', 'c9797234-1994-4054-a3fa-2b014231efaf', '037f780a-8f39-4b55-8fe0-b30d49362bda', 'e4e6cab5-32ff-49ce-911f-b45361934716', 'fc62134e-142e-4401-bc2c-8ae9fad7a983', 'c299fbbd-0875-4c28-ab7e-04c24bfece23', 'b9eacef0-3fc3-496a-9bb2-22514b851080', '645d5e31-492d-4b50-a0ed-44e159250953', '7b3ef8c4-8873-4077-b7d8-947890036ee9', 'e2b08e5b-59da-4ee0-ac34-480547186032', '2efba053-58a9-4f64-bd0c-45dd0cdcd4f5', '324e3f96-b609-4db1-99cb-d46edbc0b8ad', 'e1c14ced-c952-48a1-80de-e94e2e51a024', '15be3f03-4634-464c-8550-3b49d886ea55', '70bc735b-4d37-4e0d-8c32-436ca846eefb', '56defe1c-ea22-4937-9360-e09bc0ff1b5c', '22136949-96e8-42a7-b8b6-a0831e02574c', '51adb60f-e96f-42dd-ae74-2a48082772b1', '5fce94b8-b09a-43f3-9211-1745fe241fb2', 'b128ef10-b91c-4249-9115-b175279ca6e2', '38f66f7b-8f96-4e24-a5ae-61568e84b95b', 'a2a98bb9-66c0-4b1b-a334-173bbac97fe6', '49514a60-d146-4e9b-b2cc-83f46da73993', '2c6e13ee-fc11-479a-8a94-d2b0fe6a36dc', '56cddc7a-dde8-4cdb-89d9-724b5bfbffa1', 'ddece4f4-6c3d-403f-8968-5eb33a235f17', '6e49ac17-1661-47ba-88af-c89733b62068', 'f5111dc2-f502-4ac0-a8e5-bdda41f8cf4c', 'fd14d33e-dfde-44fa-b732-b6444ab3e32d', '26afb4a8-b384-4281-b30a-1a3fb852cb53', '2d9654e7-e89e-40b6-b952-b7579491353a', 'e63f3856-b36d-46be-89ec-56cf1b941179', '4bd36942-f85a-4483-ae66-f7680aba4c7d', 'e20edf69-67f2-4348-9f11-d41c450e7ed5', '7801ecb7-6c75-45ae-802a-9ce51b983c1e', 'bba69fe6-fc2b-481d-a8aa-6b44bc807ac4', '4f720214-8ce2-4c84-a19d-7a03a7561bf6', 'e0f28f96-dbf5-4f3b-8313-b35534bcd4a7', '6935f804-05b9-41fd-8eb2-bc226a2b0e11', '92469bd1-8b11-4bb6-b8a7-baae165aff42', '834f7edc-97d0-412e-a1ff-09f2f337cd01', '18852415-c423-48e4-a6bc-5a7be46b1f72', '88e3781c-990b-4329-9717-8eaa99a53c0c', 'ec1fcff2-f92e-4690-87be-7a03ef60a45a', '2b1fd44a-6a33-4263-8212-0bd8abc6a94f', '1f1a4082-83cd-4605-a42e-739f692f3aca', '70eb57c5-c0dc-4ec9-850e-1df5ef08de4d', 'f8ae5235-011c-4239-b947-a94c9aca5ac5', '12b80720-cbdb-499b-9347-d2dfec8a822c', '96124fc3-3c71-4bdf-88b7-ea40fae2dbb1', '8122ec06-433a-4cda-829e-72925bff82ce', '43302ee9-c2e1-47ad-8c5d-0daa7d8476af', '51d7152e-4613-446d-85bf-da5eeb4bf997', '3d767ed8-c7d3-4f10-b32a-09065977f9b9', '8e4fbbc9-db0b-47b4-a2da-4cda733fbbb4', 'ba7374bc-a0ad-4cb2-a0e6-0ef518505b03', 'fbb726f5-d627-4da7-8a17-468407713d69', '21498491-6087-44cc-aee3-ffe46153b029', 'cd603300-cd81-4b39-a543-f9c281e88b58', '36e30958-e954-4859-9b56-3c5b712660de', 'd237e9fd-f933-4cb5-ad0d-7025f98190d6', '42f4f92a-45bd-4087-9d3d-bc83da5fa0f8', 'bf608331-088e-4dc9-a909-2dbeaa537836', '984a1847-f2b3-424b-9734-0a2fe876b605', '17243de3-d450-4aae-a1e7-8ac681d3bdb6', 'dbe249cf-5568-40a5-8d7a-36d4812d577f', 'f5e16af9-37fa-4041-8ba8-b2390c0b3609', 'ad657660-e89f-4b9c-b845-1164aa9fff5d', '0e45e311-506e-4f06-867c-87acb308063a', 'd35a8fea-5253-4b6b-b37a-6f57a2f0034f', 'df27387a-923e-4bb6-8963-3dbd83765e57', '0a1019da-7825-4c21-879b-4c4cef1a797e', '44eb2eca-6788-4525-ad01-c6d5a447cf9b', 'f123fca9-4f2e-4d30-8b01-77e172f5d9d4', 'fc27d690-041e-4090-bdff-978a4f5bb5e0', 'efa7466e-2ede-4a66-91c9-de352a033efc', 'b58aaa71-3951-4ccc-bbde-5d2984f00dc7', 'c25cee88-ab6f-4cdd-bda8-7ddcf86ee383', 'dfbc87d7-ac79-483d-b3ed-5ca86a82597e', '70e5237a-7e1a-4ae4-8624-96fa87eca375', '9c7fa1f6-ed63-4737-ae9d-94193ca7e7f4', 'c18f814b-1cc4-47b5-9c6e-7a4b0e9abff3', '4ba60c9a-4acc-485e-a478-44e543da60f9', 'df690c11-5a39-4adf-8e86-026f8fbb20dc', '31df4431-303c-4323-af1a-326d4a14734e', 'b96ee721-77dd-4e99-9c91-01ea90439c13', 'ebd8e6e3-d6a2-48e8-b2ee-529dc2575f5a', '118994c7-5a7c-441e-b5fa-61f75c9ebdbf', '1b39e233-af3e-4de6-9d7d-2b4789c1fd0f', 'd7632acf-38f1-4900-a485-1aa793c1254c', '4889d8af-83bb-4fc7-8d27-94c82298a785', 'ea87ac14-cfc9-43d3-92ce-52841a303db5', 'bae21390-b93d-44f6-9c64-959e9724d48b', 'd79bf155-d19d-408c-a099-5b6667cc2e71', 'e47269f2-d2b8-47cf-b557-fb7915ff15ed', '140fce5a-7a14-4fae-85c0-f4c39c30b43f', '85d1eca6-c14b-4990-b889-271f77be0bb2', '8e875287-88c9-47ec-b35e-a7c419b75049', '962d07b7-1cf1-4830-b7c0-af3f9a25b3f6', '6bd4d880-2873-484e-8f85-aebc4286b5e0', '4efdb8e2-f9db-432b-9e22-36563429d089', '7c5c0df9-d8e4-47f2-aba1-099fc9344bf0', 'ed409354-6584-4c44-ad0b-56b291d99538', 'f1f72b91-d13a-4e1a-9065-3dab4244c13c', 'a04143ae-8dee-44e1-90a8-24ea7ff539ce', '5a40cebf-29d7-4d3c-931d-1239f45e4f3e', '887eab39-5a2e-40aa-811b-957fc2e35766', '1c72923c-16a2-4f99-8f97-d1fd99ac52ed', '9b725e44-734b-4348-82de-5ba264f4aa3d', '7c2d969c-47a8-4af5-94ac-b6d7f029e44b', '213dfc90-f099-46b0-a3ca-f08a7cec993d', 'aed989f3-cfe9-40c4-a3be-002b373b9910', '9d71451f-06e0-4a7b-a374-4a34a4f285d2', 'e21989c8-44bd-452e-a1aa-f0517bf6714d', '7cd8f324-82e3-4e02-b889-f0aee68c3ece', '09d4b06e-c992-441a-8531-e4fe802718d1', 'b5db79cf-343f-4084-80c7-5cfa44376242', '8863c8a7-f6ef-4512-ac55-e4647a36ae16', '5a08d101-55a1-44e3-9a48-2afc3cf94181', 'b80b8ac3-a312-4908-922b-97885a21af11', 'e939e67d-4232-48a6-868d-527200c959eb', '6f774e2a-be0d-465c-894a-35d012cd2253', 'b1846d5a-7529-4e66-b503-b60258f778c9', '15d75e73-29bb-4bf7-80e5-66c31fabfb5c', '86f19f1e-3798-474f-a0ac-37cdea445eef', '3e2c7e3e-a8b9-4208-9857-35e26270eae3', '49f97f3a-0208-46a7-8cf8-62977aca3465', '5bb75490-9375-4e5a-bd5e-0b32f7b99fc4', '80884545-479f-41c4-b328-bdf927bb3eec', '87f750d7-bbcd-4d19-8198-d9daa13cd231', '34188fbe-f04d-4c7b-b619-18e067dce405', 'f9f9d28e-fb67-4a35-a736-763e16053100', '9ca78527-12e0-45c3-acf4-26f983e80bbd', '51863840-5b7c-4987-bb81-5a7bac5802ce', 'e24797c9-6ab1-47e3-89e7-55d404e738c8', 'e6591d3f-794c-4413-9484-98916ad0de64', '981303f2-a781-435b-9d39-d59bbbf37d53', '06e4870d-2421-41c9-b3f7-c8dd1c2bf026', '95ee08be-b067-43ac-b15f-e26b67a0ef85', '07f78cc5-8ac9-4f27-bcec-1023a7ae7829', '3e71aaca-d606-45d1-8c6f-9632ae8f7ede', 'c355e9b7-2d88-4291-8cf5-2ed8cbf26348', 'c987c3fe-dc18-4adf-93d4-8294c198c327', '58695d86-6d6a-4a7e-a5ef-6fcda008e9fd', 'cc67f2f8-b3c9-4423-a4ca-771639ad0517', '2a4bedf6-9fbb-4e61-8b88-3e9c9ba3c2bc', '17bfea60-66fc-409b-a42c-e03f03fb04dc', '1847141b-a68f-495f-b6b4-d8e695921881', '8e35d28c-90f9-41f2-9f83-f0b5ed91c92c', 'aea4205d-5d1a-4b23-9000-ddeeba9b6b95', '4ce1f0ee-7c6f-4198-9a50-5aa1672b0271', '9a2db13c-c7dd-4570-86e2-63fc94a4fa58', '20542391-19c6-4d8a-a1f3-fab6071ecb62', '5d087f3b-f8e6-4e48-9d17-2fdd8efba69a', '0fbf8b1f-ee90-404c-98f3-c97f6c910caa', '11297285-3aa8-4cc5-a8b2-8ea1d6719846', '58e532bf-7901-4f62-8fce-f82c0d7c0556', '37f92cfc-0382-4898-b2a6-7c62ece2cd12', '021c49b5-aad2-4af6-87cc-21afadc38ed6', '10bea781-8e6c-4c30-a6d5-d05d0595b852', 'dbfb18c9-4cac-46e1-899f-5e32796aaf3a', '26b5f246-08b9-4110-aea1-1789440015c1', 'c99949d8-7900-42d4-b994-c0ba83e102e0', 'a81feecc-57d4-408a-ba20-17716d66c565', 'ce331117-6008-4659-aacf-ec3ff6bba022', 'f68061d0-9da5-4188-8eb1-f904d9019d1f', '4efd6621-6723-492f-8e4e-67b742a362ce', '37cdaa41-b70f-42ce-af7f-762bf4f732b4', 'c8440636-fe03-4fa6-9dee-48ee528c0030', '4a870de5-853d-467d-8347-8fe5d5199581', '8f98a768-d21d-4a80-aec1-a94e32aa451b', '3750fb68-b21f-4cc7-88bb-259dbd8a48cf', 'b603262b-9b11-48a7-9790-ffc50e0795d2', 'fde6efac-8c6a-4a6e-bfad-d868f3b7f5fa', '865eb0dc-d880-4346-8735-6d6c96640daa', 'e46b5150-e60a-4acf-b2ee-34928d0040f6', 'c3ba195f-e06d-4ede-99a2-3a736c5eb301', '90d955a4-18f3-4766-aad3-f3b5dde232a1', '486d80cb-da0c-41de-9713-05c8fe7e914a', '9c317750-514c-46f0-8b54-5fbba36cc701', '18f55e8f-a712-4dcf-8a54-6c68df5ba302', 'ee3c10d1-ddc5-438a-a95d-ff06a1b9baa7', '943eecc2-521a-46a2-8cb8-2397be182302', '2195fcaf-4b67-4f24-b87c-78ae0bcada44', 'cb5ed840-bdca-446a-a178-8901ea002e1d', '5a6f261c-1bab-45b8-8290-4ad4d6cec5ec', '38722eca-3f77-4fe6-9284-074e2e13bb69', '527f5bb9-514c-4d5d-9131-23bd8feeccfd', 'd91b7a98-8de8-4f0b-8af0-2ab4a7aab38d', 'fae888cb-5ab2-4d07-8cae-01da2f397384', 'd6b8c1c9-5764-4478-b34f-07801e38eb91', 'b8f7f50d-669e-4a5a-a651-7e7446d08eef', 'f52a20a4-ef45-41d8-9bfd-a52dd7f99424', 'd07408ad-a647-46a1-9ab5-2084a143be30', '9423ad6d-a739-46d8-82c6-e1bc5fc6aa7b', '03ab6b73-f669-4994-9008-a7ae1770c268', '31d36b90-526e-4da2-b9f7-211ede0edf49', 'f6cfd8a1-88d8-442d-947e-cf8c86ba0c22', 'ffc4dc99-eae8-46b0-abcd-5bb54abfc60b', '7eb28049-de6f-4b47-af6b-6a049026b8dc', '98aee7af-2645-4f47-8c41-0b6a53173605', '7f1c26fa-a02d-4ce0-9c4b-c362e9fd8867', '16ace52c-b447-41d5-955d-df244f2e4da3', '62054a95-2c27-474d-bbd6-533afc68264c', '54ed8c48-fb34-4c7a-9abc-b6e8f3c2bfcb', '6bfd7cfc-7249-4e42-bd90-5639c24671b7', '1df9277b-ea04-49c1-a593-fd84a008f107', '265c31ff-5c0a-4f3c-ab6d-3521f6346992', '2ca4f1f9-39d9-4cf7-bffc-b3aa213eea65', 'ee871bce-0351-414b-a7c9-764f623561d2', '424720e7-3452-44e6-901f-d3ea2b2ba3eb', '9c6c7c01-f6c7-4b9a-9246-07b8c3a13c74', 'd5b396ca-2551-4110-9982-d67be03e105a', '496f59ef-330d-49de-8ad5-61f66de81c3a', '8632de5f-59b1-480c-9ca8-47e0c8f49afc', '18d2390a-99ba-4c08-8b91-680a4b9cdab2', 'ebcc3902-2656-43bd-8688-7d1d725ad48c', '9ea737ef-286d-4762-a3ca-35f40d0fe136', 'd6c8b079-f778-4e3b-9db1-68427b1d9aac', 'b195ee9c-e80a-4a95-acfd-b49681c5526a', '6204ef94-7857-4cd4-8c12-8699a7a07fa3', '4a3f6a59-381e-4bd6-9837-474e260eb873', '4611a545-dbd4-4700-b48b-c2c5629acb28', '59399af2-2fb2-4190-8eb6-334fd45e6e71', '2732c052-2512-49bb-99b2-3072e465176b', '6664bb4b-8e1f-490e-a412-f226746bc021', '50ba1e6e-eff0-4e60-8e1f-b8faa5b560b9', '39a49bfb-6988-43ae-a9b7-8e0ad8ad7809', '4816fcc9-bf65-47dd-819f-3ace51ac9064', 'fc3461fd-ef63-4696-a0df-5fe96d11d45e', '6419c0ee-f1a8-4169-b0b1-530fd9977089', 'c23a6079-7c7d-4209-8ea1-07bd20d1f07c', '579d607d-966a-473a-acc4-296dec58c6c6', '5b547cdb-ec94-40a4-b579-a25d7f1866d5', '7c0d4e5c-7172-4766-9deb-2e7727cf0742', '535b2f96-3ae5-4e97-ad8d-e1d6b31771a2', '1c94697f-5139-48f5-97b5-18676aa11bce', '0372b8bf-5060-4529-a251-a885a9476752', '82697fda-ec36-4429-ac2d-4b7a55882605', 'e85bd930-5b95-47ed-99bd-f7cae9ea23d6', '8a1b8f28-8125-4be9-9367-bda8ebbeeadb', 'eff391c0-8676-45bd-97e4-e9b4550b618e', '478ed5fa-4250-43ae-a022-16e1e9a399fb', 'ecc97fdf-311c-45f9-be09-3a397bff6c66', '2f96fcba-8fcb-461f-987b-9bd57f4e55e4', '957595de-d300-42f2-810d-60f4feca2f5e', '575438b0-da4e-42b3-ae81-849e9c993b3f', 'db900d89-ae47-479f-816b-9834ed45d652', 'd4eb0d32-6c0c-46ce-af2f-e69174cb5f64', '36fd03e9-b577-40a4-b228-931cebd24aea', '102f386d-6bae-441b-8e01-7e9cde291d7d', 'ec7e9e16-f14b-490b-b1b2-951b65461667', 'dfd1d3c7-67ae-48d4-a1c4-21d154a168c9', '75661277-3e77-4d96-9410-19fcc74d5dff', '14205d5a-008d-4240-a77e-13e05e9dd876', '19eea3d5-661d-4aea-9db3-1c37e1a6bc1f', '1f6f849d-2d38-4efa-98d8-d53a3503c21c', 'b3442b85-3c28-4ee3-93a6-ed9390a9d9d4', '90a2fa11-b717-4567-87c3-10ed34d72361', '7332f55d-574f-4d44-9972-dee0758891b8', 'ee6dd02b-7d5a-473e-b21b-3dbce78ea678', 'b02b775f-e742-4021-ba08-a84f7492a5a2', '2e684242-9557-4010-a3b7-24429c7fdfeb', 'e6f7924c-8966-410e-bdd2-1a6cba877167', 'b1bd9d69-a7ce-4ab7-b993-169ba51a890c', '9781e18c-e357-497d-b6f5-648940294a69', '064fcdc9-0d5b-471d-9d50-618319131fe1', '43dc7da5-4761-40e1-9d0d-6a83c6198e35', '1718abcd-584c-4e62-aea4-cadf5d32b48a', '01b88b82-c13e-476a-94fc-3e913a0322eb', '6f164ff5-554c-464e-8585-9d164e6ca23c', '25407234-1782-41ce-9d5f-941c3b15c69c', '987c938c-5aad-4d94-a41b-7987ed408276', '9cd6795a-4f1f-4a5d-81a0-b697a5dc7757', 'fef47bb7-5b64-4da4-a1c1-f0bfd4595453', '010171cb-ddda-456d-93a1-ddbfde7b4586', 'a67592bd-70f2-4a47-8fe1-02b711420114', '63e1ee94-81bd-40f6-9329-f4139c6c83d9', 'ab837f8a-76f5-456a-bbe9-15583030f079', 'd8e9fce5-9373-499d-a189-f50d79521745', '1f8c035b-9a9b-4906-ad2b-7edeb95360ee', '2016c9e4-72e5-4e8e-a3ab-779c346fae02', '60d82e3b-d6c3-47d4-8557-f1b02fe4c152', 'e9c77f92-53a7-4c74-bd4c-938ffe8aeab5', '6d7cd9b6-58c0-4537-b08e-a834d838631c', '1faa9e32-294e-42dd-9b3e-70a1440b92a0', '6818f7e2-8eed-4f56-bb65-733e2ac28861', 'b193f6e4-8f8a-44f9-86c5-c4d4f1e51347', 'a43d71f4-f946-4eae-bcd2-755c66edec5b', 'c038f899-5b5f-46d0-8eac-5831109e9850', '87796bed-fc5d-4df7-a8a2-fa07ec323962', 'f1bdcc7c-da0b-4957-a231-c404424c4fd1', 'e317c706-b3a5-41e9-a2dd-97b8fac614e0', '85dc039c-b48b-4a23-84b4-edc717baefd5', '94567d11-45bb-4efa-8ab9-dea3a823cfc0', 'b5751bcd-b445-4192-8ea0-1ca47fca9c4e', '8b567aef-3efd-4d45-850f-e099107d2603', 'f6e4f993-3441-4be6-8e62-d4fd3efbbe8d', 'bf4c47a9-39ae-43ee-8445-347e0da71c8c', '7b3947b2-5747-4af3-9e09-aa61a03a8942', '1c49b97f-81df-4eb2-9cc6-3fb4c8dff11e', '26d6945b-cf70-4810-82f0-314b29637f8c', 'b26b52f1-5934-434e-904b-7c2b72321d04', '97cf7ffb-2f6d-457c-b1c2-05ccd5eb83ea', 'c648e422-6cc8-4ba8-9ca9-e0bab47b62c6', 'c5fb2434-b0e4-4666-adb8-5cc3a05593eb', '2edb4517-e1fb-41ac-85c2-149c00abc6e5', '21589389-1765-4b49-9fb8-49c06a0dc3a1', '341ae0c5-5f72-46b7-8030-d33a9f36e50b', '683648cc-ae8b-421d-83a5-0fe6b6070852', 'b5206540-542e-4bc8-a3e1-359190830176', 'f465c35b-c740-4308-a4d5-bd1516d5803e', '31723397-7b7b-432c-8eb5-c6104ff7873f', '198cbf2c-6a22-4ccb-805c-d3762c50657b', '8e1c49a0-4e99-46b5-89fd-93e2a9d6f9a1', 'ab389bd6-c8ad-4cda-ba8b-88f02e1ef96a', '88fe4bc4-2875-414d-b575-f06d79a333b9', '5b79d0a4-80f6-4581-9676-78deb7210247', 'dd11b560-6870-46d7-b369-2d6dccba3692', '4dc56998-50aa-4210-b2c1-94a482622371', '439bac60-7c47-4bb4-a9b1-33da8089d3ff', 'ca0a4c08-f7ee-4f10-89a5-ba6acf42bbd5', 'ed2ca39d-3353-48ae-8883-4619625a85a1', '6f9774cd-592d-4b23-b306-b0beebc49cfd', 'e68e6937-0b83-41df-acfe-57c5bef0a559', '4b3438a8-b498-4bd4-bf7e-aee2af0c059e', '84b658b3-9987-4b98-a72c-392153acddcd', 'f15691c4-2be7-4f2c-b435-ba12e27f36bd', '080f5323-b09c-4bcb-9127-b5b81bead404', 'c74632f4-62ed-4965-88c5-1471d3345b32', 'bef88783-7476-459f-86e4-5075eabbe1d7', '0dfbc800-4b06-4bf1-898b-7d79a47e62cb', '69349620-5653-4616-8244-6fd59eba5296', '6ac468a2-d53e-4b2d-a95f-5e68bdfa6fd7', '3fcede10-4a9f-4f60-9206-8dd644a0c736', '778b91b3-3bed-4217-964c-6cea30d3dc30', 'f8f07ebe-2312-4ad0-b43f-1ce1f0e3135d', 'cfcc8fde-8b72-4929-9e20-44b9417e0330', 'b2ee2254-7e5b-4f87-9c14-9688e5778ba3', 'f1a07789-244f-4271-a21f-e07800dc637a', 'bb2188df-c43e-41d3-bb9c-11949b437aa8', 'fdd47191-da95-4d5e-9010-eeaca4f71f43', '812247e2-46ef-4f09-8391-067b714c1d78', '4a94730e-9f74-422f-8145-f1344e60de10', '7c707670-5632-4d29-ab5c-8d4fab11bb9b', '54304097-c005-4e0b-bd2a-020f08216c97', '393a6d1a-4746-42dc-94d0-d053e37424f9', 'ee900cc3-a13d-4aa4-a28c-85b2386f3fcf', '1823e153-d25a-4ea6-8899-eacd88b6ef82', '417413ca-96b4-49b2-8999-00e5e73dc130', 'd35ac5fa-7cb7-451d-9d9e-d38958cf75f9', 'ff4c8543-db3f-44c5-b952-eb9808ea29cc', 'aec2511a-0a93-47ef-9cee-d81159e3ff1d', '93275fb8-b3a9-45e7-9400-da35f71c0b1c', '511645e1-784c-4f08-9dfa-ee006eb009b7', 'bc92de9b-c6a8-4219-98c0-3f73998ad1ea', '6ee96290-faee-4f64-a496-000861ea4247', 'fe1dfc77-1b4f-4c84-9dd4-85a00d4fa6ee', '1229a917-17d6-421b-9293-1fd77d40b4ea']+task_ids
# task_ids=['ebce4c06-4d56-4700-8030-f2433bf5704b']
print(len(task_ids))
error_ids = []
for id in task_ids:
    url = get_image_url(id)
    if url:
        dowmload_image(url, '')
    else:
        error_ids.append(id)
print(error_ids)
