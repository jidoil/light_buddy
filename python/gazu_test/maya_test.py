from maya import cmds

SUFFIXES = {
    "mesh": "_mesh",
    "joint": "_jnt",
    "camera": None
}
DEFAULT_SUFFIX = "_grp"


def rename(selection=False):
    """
    선택한 오브젝트의 이름을 변경합니다.
    rename of selected objects
    Args:
        selection (bool): True로 설정하면 선택한 대상의 이름을 변경 합니다.
                          False로 설정하면 모든 대상의 이름을 변 합니다.
    Returns:
        list: 이름이 변경 된 오브젝트들의 이름이 포함된 리스트를 반환합니다.
    """
    objects = cmds.ls(selection=selection, dag=True, long=True)

    if selection and not objects:
        print("you have no object selected")

    for obj in objects:

        short_name = obj.split("|")[-1]

        children = obj.listRelatives(obj, children=True) or []  # 부모나 자식의 노드들을 list로 반환하는 함수

        if len(children) == 1:
            print("only child", short_name)
            child = children[0]  # object타입을 얻기 위해 자식 노드가 1개인 오브젝트를 분리한다.
            objType = cmds.objectType(child)
        else:
            print("[] or 1++ children", short_name)
            objType = cmds.objectType(obj)  #

        suffix = SUFFIXES.get(objType, DEFAULT_SUFFIX)

        if not suffix:  # suffix의 대상이 아닌 파일들을 스킵한다.
            continue

        if short_name.endswith("_" + objType):  # 중복으로 suffix를 입력하는 것을 방지한다.
            continue

        new_name = "%s_%s" % (short_name, suffix)  # 변경할 이름을 만들어준다.

        cmds.rename(short_name, new_name)  # 이름을 변경한다.

        return objects  # 이름이 변경된 리스트를 반환한다.

def gearCreator(teeth=10, length=0.3):
    """
    기어 오브젝트를 생성하는 함수
    Args:
        teeth (int): 생성할 기어의 톱니 수.
        length (float): 기어의 길이

    Returns:
        tuple: 생성된 기어의 변환 노드, 폴리곤 파이프 생성노드, 폴리곤 익스트루드 생성 노드
    """
    spans = teeth * 2

    transform, creator = cmds.polyPipe(subdivisionsAxis=spans)  #

    side_faces = range(spans * 2, spans * 3, 2)
    cmds.select(clear=True)  # 현재 선택한 모든 오브젝트를 선택해제함
    for face in side_faces:
        cmds.select('%s.f[%s]' % (transform, face), add=True)

    extrude = cmds.polyExtrudeFacet(localTranslatZ=length)[0]

    return transform, creator, extrude  # extrude를 저장하지 않으면 다시 재선택해야하는 번거로움이 있다.

