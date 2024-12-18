from ttp import ttp

data = """
VLAN  Name                 Status    Ports
----- -------------------- --------- ----------------------------------------
1     System-VLAN          active    Gi1/0/48, Gi1/0/49, Gi1/0/50, Gi1/0/51,
                                     Gi1/0/52
85    N/A                  active    Gi1/0/48, Gi1/0/49, Gi1/0/50, Gi1/0/51,
                                     Gi1/0/52
86    N/A                  active    Gi1/0/48, Gi1/0/49, Gi1/0/50, Gi1/0/51,
                                     Gi1/0/52
87    HN                   active    Gi1/0/1, Gi1/0/2, Gi1/0/3, Gi1/0/4,
                                     Gi1/0/5, Gi1/0/6, Gi1/0/7, Gi1/0/8,
                                     Gi1/0/9, Gi1/0/10, Gi1/0/11, Gi1/0/12,
                                     Gi1/0/13, Gi1/0/14, Gi1/0/15, Gi1/0/16,
                                     Gi1/0/17, Gi1/0/18, Gi1/0/19, Gi1/0/20,
                                     Gi1/0/21, Gi1/0/22, Gi1/0/23, Gi1/0/24,
                                     Gi1/0/25, Gi1/0/26, Gi1/0/27, Gi1/0/28,
                                     Gi1/0/29, Gi1/0/30, Gi1/0/31, Gi1/0/32,
                                     Gi1/0/33, Gi1/0/34, Gi1/0/35, Gi1/0/36,
                                     Gi1/0/37, Gi1/0/38, Gi1/0/39, Gi1/0/40,
                                     Gi1/0/41, Gi1/0/42, Gi1/0/43, Gi1/0/44,
                                     Gi1/0/45, Gi1/0/46, Gi1/0/47, Gi1/0/48,
                                     Gi1/0/49, Gi1/0/50, Gi1/0/51, Gi1/0/52
399   N/A                  active    Gi1/0/48, Gi1/0/49, Gi1/0/50, Gi1/0/51,
                                     Gi1/0/52
497   N/A                  active    Gi1/0/24, Gi1/0/48, Gi1/0/49, Gi1/0/50,
                                     Gi1/0/51, Gi1/0/52
498   N/A                  active    Gi1/0/48, Gi1/0/49, Gi1/0/50, Gi1/0/51,
                                     Gi1/0/52
"""

template = """
<group name="vlans">
VLAN  {{ VLAN | DIGIT }}  {{ Name | WORD | default("N/A") }}  {{ Status | WORD }}  {{ Ports | PHRASE }}
{{ _start_ }}
<group name="ports">
                                     {{ Ports | PHRASE }}
</group>
</group>
"""

parser = ttp(data=data, template=template)
parser.parse()
result = parser.result()

import pprint
pprint.pprint(result)
