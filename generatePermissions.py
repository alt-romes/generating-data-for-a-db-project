from zeroPlayerGame import DBC

INSERT_INTO_PERMISSIONS = "insert into permissions values ('{}')"
INSERT_INTO_HAS_PERMISSIONS = "insert into parent values('{}','{}')"

def generatePermissions():

    idsAdded = []

    with open("permissions.txt", "r") as f:
        lines = f.readlines()

    for l in lines:
        aux = l.strip().replace('-', '').strip()
        if aux not in idsAdded and aux != '':
            idsAdded.append(aux)
            DBC.printAndExecute(INSERT_INTO_PERMISSIONS.format(aux))


    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            iDeep = len(lines[i].split(" ")[0])
            jDeep = len(lines[j].split(" ")[0])

            if iDeep == jDeep-1:
                DBC.printAndExecute(INSERT_INTO_HAS_PERMISSIONS.format(lines[i].strip().split(" ")[1], lines[j].strip().split(" ")[1]))
            elif iDeep >= jDeep:
                break