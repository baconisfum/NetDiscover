#
# Name: Gavin Claire, Ronald Du, Chad Saltzman
# Document: views.py
# Decription: Views for the website.
#
from django.shortcuts import render
from website.python.DeviceDiscovery import *
from website.python.Comparison import *
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from django.core import serializers
import json

import logging as logger

TESTING = False


test1dict = {'192.168.111.129': {
    "IP": "192.168.111.129",
    "device_type": "Router",
    "hostname": "Router1",
    "interfaces": {
        "FastEthernet0/0": {
            "IP": "10.0.0.1/30",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "",
            "speed": "",
            "type": "",
            "vlans": []
        },
        "FastEthernet0/1": {
            "IP": "192.168.111.129/24",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "",
            "speed": "",
            "type": "",
            "vlans": []
        },
        "FastEthernet1/0": {
            "IP": "10.0.0.5/30",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "",
            "speed": "",
            "type": "",
            "vlans": []
        }
    },
    "local_mac_address": [
        "c401.0655.0000",
        "c401.0655.0001",
        "c401.0655.0010"
    ],
    "model": "3700",
    "neighbors": [
        "10.0.0.6",
        "10.0.0.2",
        "192.168.111.1",
        "192.168.111.254"
    ]
}, '10.0.0.6': {
    "IP": "10.0.0.6",
    "device_type": "Router",
    "hostname": "Router3",
    "interfaces": {
        "FastEthernet0/0": {
            "IP": "10.10.20.1/24",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "",
            "speed": "",
            "type": "",
            "vlans": []
        },
        "FastEthernet0/1": {
            "IP": "10.10.30.1/24",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "",
            "speed": "",
            "type": "",
            "vlans": []
        },
        "FastEthernet1/0": {
            "IP": "10.0.0.6/30",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "",
            "speed": "",
            "type": "",
            "vlans": []
        },
        "GigabitEthernet0/0": {
            "IP": "",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "GigabitEthernet0/0",
            "speed": "",
            "type": "",
            "vlans": []
        },
        "GigabitEthernet0/1": {
            "IP": "",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "GigabitEthernet0/1",
            "speed": "",
            "type": "",
            "vlans": []
        }
    },
    "local_mac_address": [
        "c403.07eb.0000",
        "c403.07eb.0001",
        "c403.07eb.0010"
    ],
    "model": "3700",
    "neighbors": [
        "10.10.20.10",
        "10.10.30.10",
        "Router1",
        "Router1"
    ]
}, '10.0.0.2': {
    "IP": "10.0.0.2",
    "device_type": "Router",
    "hostname": "Router2",
    "interfaces": {
        "FastEthernet0/0": {
            "IP": "10.0.0.2/30",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "",
            "speed": "",
            "type": "",
            "vlans": []
        },
        "FastEthernet0/1": {
            "IP": "10.10.10.1/24",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "",
            "speed": "",
            "type": "",
            "vlans": []
        },
        "FastEthernet1/0": {
            "IP": "10.157.0.1/24",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "",
            "speed": "",
            "type": "",
            "vlans": []
        },
        "GigabitEthernet0/1": {
            "IP": "",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "GigabitEthernet0/1",
            "speed": "",
            "type": "",
            "vlans": []
        },
        "GigabitEthernet1/0": {
            "IP": "",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "GigabitEthernet1/0",
            "speed": "",
            "type": "",
            "vlans": []
        }
    },
    "local_mac_address": [
        "c402.07c0.0000",
        "c402.07c0.0001",
        "c402.07c0.0010"
    ],
    "model": "3700",
    "neighbors": [
        "10.157.0.10",
        "10.10.10.10",
        "Router1",
        "Router1"
    ]
}, '192.168.111.1': {
    "IP": "192.168.111.1",
    "device_type": "Desktop",
    "hostname": "192.168.111.1",
    "interfaces": {},
    "local_mac_address": [],
    "model": "None",
    "neighbors": []
}, '192.168.111.254': {
    "IP": "192.168.111.254",
    "device_type": "Desktop",
    "hostname": "192.168.111.254",
    "interfaces": {},
    "local_mac_address": [],
    "model": "None",
    "neighbors": []
}, '10.10.20.10': {
    "IP": "10.10.20.10",
    "device_type": "Switch",
    "hostname": "Switch2",
    "interfaces": {
        "FastEthernet0/0": {
            "IP": "",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "FastEthernet0/0",
            "speed": "",
            "type": "",
            "vlans": []
        },
        "Vlan10": {
            "IP": "10.10.20.10/24",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "Vlan10",
            "speed": "",
            "type": "",
            "vlans": []
        }
    },
    "local_mac_address": [
        "0ca9.330b.800a"
    ],
    "model": "vios_l2",
    "neighbors": [
        "Router3",
        "Router3",
        "10.10.20.100",
        "10.10.20.200"
    ]
}, '10.10.30.10': {
    "IP": "10.10.30.10",
    "device_type": "Switch",
    "hostname": "Switch3",
    "interfaces": {
        "FastEthernet0/1": {
            "IP": "",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "FastEthernet0/1",
            "speed": "",
            "type": "",
            "vlans": []
        },
        "Vlan10": {
            "IP": "10.10.30.10/24",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "Vlan10",
            "speed": "",
            "type": "",
            "vlans": []
        }
    },
    "local_mac_address": [
        "0ca9.33f8.800a"
    ],
    "model": "vios_l2",
    "neighbors": [
        "Router3",
        "Router3",
        "10.10.30.100",
        "10.10.30.150",
        "10.10.30.200"
    ]
}, '10.157.0.10': {
    "IP": "10.157.0.10",
    "device_type": "Switch",
    "hostname": "Switch0",
    "interfaces": {
        "FastEthernet1/0": {
            "IP": "",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "FastEthernet1/0",
            "speed": "",
            "type": "",
            "vlans": []
        },
        "Vlan10": {
            "IP": "10.157.0.10/24",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "Vlan10",
            "speed": "",
            "type": "",
            "vlans": []
        }
    },
    "local_mac_address": [
        "0ca9.331d.800a"
    ],
    "model": "vios_l2",
    "neighbors": [
        "Router2",
        "Router2"
    ]
}, '10.10.10.10': {
    "IP": "10.10.10.10",
    "device_type": "Switch",
    "hostname": "Switch1",
    "interfaces": {
        "FastEthernet0/1": {
            "IP": "",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "FastEthernet0/1",
            "speed": "",
            "type": "",
            "vlans": []
        },
        "Vlan10": {
            "IP": "10.10.10.10/24",
            "description": "",
            "destination_IP": "",
            "destination_port": "",
            "duplex": "",
            "macs": [],
            "mode": "",
            "port_name": "Vlan10",
            "speed": "",
            "type": "",
            "vlans": []
        }
    },
    "local_mac_address": [
        "0ca9.3339.800a"
    ],
    "model": "vios_l2",
    "neighbors": [
        "Router2",
        "Router2",
        "10.10.10.100",
        "10.10.10.200"
    ]
}, '10.10.20.100': {
    "IP": "10.10.20.100",
    "device_type": "Desktop",
    "hostname": "10.10.20.100",
    "interfaces": {},
    "local_mac_address": [],
    "model": "None",
    "neighbors": []
}, '10.10.20.200': {
    "IP": "10.10.20.200",
    "device_type": "Desktop",
    "hostname": "10.10.20.200",
    "interfaces": {},
    "local_mac_address": [],
    "model": "None",
    "neighbors": []
}, '10.10.30.100': {
    "IP": "10.10.30.100",
    "device_type": "Desktop",
    "hostname": "10.10.30.100",
    "interfaces": {},
    "local_mac_address": [],
    "model": "None",
    "neighbors": []
}, '10.10.30.150': {
    "IP": "10.10.30.150",
    "device_type": "Desktop",
    "hostname": "10.10.30.150",
    "interfaces": {},
    "local_mac_address": [],
    "model": "None",
    "neighbors": []
}, '10.10.30.200': {
    "IP": "10.10.30.200",
    "device_type": "Desktop",
    "hostname": "10.10.30.200",
    "interfaces": {},
    "local_mac_address": [],
    "model": "None",
    "neighbors": []
}, '10.10.10.100': {
    "IP": "10.10.10.100",
    "device_type": "Desktop",
    "hostname": "10.10.10.100",
    "interfaces": {},
    "local_mac_address": [],
    "model": "None",
    "neighbors": []
}, '10.10.10.200': {
    "IP": "10.10.10.200",
    "device_type": "Desktop",
    "hostname": "10.10.10.200",
    "interfaces": {},
    "local_mac_address": [],
    "model": "None",
    "neighbors": []
}}



def home(request):
    # devices_dict = request.session.get('devices_dict', '')
    # devices_dict = importDeviceData(str(request.FILES['myfile']))
    

    # try:
    devices_dict = importDeviceData(json_string = request.session.get('devices_dict', ''))
    
    if devices_dict == None:
        request.session['devices_dict'] = str(test1dict)
            # devices_dict = importDeviceData(json_string = request.session.get('devices_dict', ''))
        
        
    # except:
        
        # pass
    
    return render(request, 'home.html')

def inspectUpload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        devices_dict = importDeviceData(str(request.FILES['myfile']))
        request.session['devices_dict'] = str(devices_dict)

        nodeData = str(devices_dict)
        nodes = getNodes(devices_dict)
        edges = getEdges(devices_dict)
        return render(request, 'inspect.html', {'nodes': json.dumps(nodes), 'edges': json.dumps(edges), 'nodeData': nodeData.replace("'", '"')})
    # try:
        
    # except Expection as e:
    
def upload(request):
    return render(request, 'upload.html')
    
def inspect(request):

    
    # devices_dict = importDeviceData(json_string = request.session.get('devices_dict', ''))
    try:
        devices_dict = importDeviceData(json_string = request.session.get('devices_dict', ''))

    except:
        devices_dict = None
        pass

    if not TESTING:
        if  devices_dict:

            nodes = getNodes(devices_dict)
            edges = getEdges(devices_dict)

     
            return render(request, 'inspect.html', {'nodes': json.dumps(nodes), 'edges': json.dumps(edges), 'nodeData': str(devices_dict).replace("'", '"')})
        else:
            return render(request, 'upload.html')
    else:
        with open("test.json") as json_file:
            nodeData = json.load(json_file)

        devices_dict = importDeviceData("test.json")
        request.session['devices_dict'] = str(devices_dict)
        nodes = getNodes(devices_dict)
        edges = getEdges(devices_dict)
        
        return render(request, 'inspect.html', {'nodes': json.dumps(nodes), 'edges': json.dumps(edges), 'nodeData': nodeData.replace("'", '"')})

def edit(request):

    try:
        devices_dict = importDeviceData(json_string = request.session.get('devices_dict', ''))

    except:
        devices_dict = None
        pass

    if not TESTING:
        if  devices_dict:

            nodes = getNodes(devices_dict)
            edges = getEdges(devices_dict)

            return render(request, 'edit.html', {'nodes': json.dumps(nodes), 'edges': json.dumps(edges), 'nodeData': str(devices_dict).replace("'", '"')})
        else:
            return render(request, 'upload.html')
    else:
        with open("test.json") as json_file:
            nodeData = json.load(json_file)

        devices_dict = importDeviceData("test.json")
        request.session['devices_dict'] = str(devices_dict)
        nodes = getNodes(devices_dict)
        edges = getEdges(devices_dict)
        
        return render(request, 'edit.html', {'nodes': json.dumps(nodes), 'edges': json.dumps(edges), 'nodeData': nodeData.replace("'", '"')})

def compare(request):

    try:
        compare_dict1 = importDeviceData(json_string = request.session.get('compare_dict1', ''))
        compare_dict2 = importDeviceData(json_string = request.session.get('compare_dict2', ''))
        comparison_dict = compareTopologies(compare_dict1, compare_dict2)
        nodesWhite = getNodes(comparison_dict["compTopology"], "")
        nodesRed = getNodes(comparison_dict["missTopology"], "Red")
        nodesGreen = getNodes(comparison_dict["newTopology"], "Green")

        edgesWhite = getEdges(comparison_dict["compTopology"])
        edgesRed = getEdges(comparison_dict["missTopology"])
        edgesGreen = getEdges(comparison_dict["newTopology"])

        nodes = (nodesWhite + nodesRed + nodesGreen)
        edges = (edgesWhite + edgesRed + edgesGreen)

    except:
        compare_dict1 = None
        compare_dict2 = None
        pass

    nodeData = compare_dict1
    if nodeData is not None:
        nodeData.update(compare_dict2)

    if not TESTING:
        if  compare_dict1 and compare_dict2:

            return render(request, 'compare.html', {'nodes': json.dumps(nodes), 'edges': json.dumps(edges), 'nodeData': str(nodeData).replace("'", '"')})
        else:
            return render(request, 'comparisonUpload.html')

def comparisonUploadNew(request):
    return render(request, 'comparisonUpload.html')

def comparisonUpload(request):

    if request.method == 'POST' and request.FILES['myfile']:
        compare_dict1 = importDeviceData(str(request.FILES['myfile']))
        nodeData = json.loads(exportDeviceData(compare_dict1, write_true = False))

    if request.method == 'POST' and request.FILES['myfile2']:
        compare_dict2 = importDeviceData(str(request.FILES['myfile2']))
        nodeData2 = json.loads(exportDeviceData(compare_dict2, write_true = False))

    comparison_dict = compareTopologies(compare_dict1, compare_dict2)

    nodesWhite = getNodes(comparison_dict["compTopology"], "") or []
    nodesRed = getNodes(comparison_dict["missTopology"], "Red") or []
    nodesGreen = getNodes(comparison_dict["newTopology"], "Green") or []

    edgesWhite = getEdges(comparison_dict["compTopology"]) or []
    edgesRed = getEdges(comparison_dict["missTopology"]) or []
    edgesGreen = getEdges(comparison_dict["newTopology"]) or []

    nodes = (nodesWhite + nodesRed + nodesGreen)
    edges = (edgesWhite + edgesRed + edgesGreen)
    request.session['compare_dict1'] = str(compare_dict1)
    request.session['compare_dict2'] = str(compare_dict2)
    
    nodeData = compare_dict1
    if nodeData is not None:
        nodeData.update(compare_dict2)

    return render(request, 'compare.html', {'nodes': json.dumps(nodes), 'edges': json.dumps(edges), 'nodeData': str(nodeData).replace("'", '"')})

def export(request):

    try:
        devices_dict = importDeviceData(json_string = request.session.get('devices_dict', ''))

    except:
        devices_dict = None
        pass

    if not TESTING:
        if  devices_dict:

            nodes = getNodes(devices_dict)
            edges = getEdges(devices_dict)

            return render(request, 'export.html', {'nodeData': str(devices_dict).replace("'", '"')})
        else:
            return render(request, 'upload.html')
    else:
        with open("test.json") as json_file:
            nodeData = json.load(json_file)

        devices_dict = importDeviceData("test.json")
        request.session['devices_dict'] = str(devices_dict)
        nodes = getNodes(devices_dict)
        edges = getEdges(devices_dict)
        
        return render(request, 'export.html', {'nodeData': nodeData.replace("'", '"')})

def help(request):
    return render(request, 'help.html')

def passDictionary(request):
    devices_dict = request.POST.get('dic', None)
    #logger.critical(devices_dict)

    request.session['devices_dict'] = str(devices_dict)

    return HttpResponse("", content_type='text/plain')

def passNetworkInformation(request):
    auth_dict = json.loads(request.POST.get('dic', None))
    # logger.critical(auth_dict)
    
    seed_IP = request.POST.get('IP', None)
    # logger.critical(seed_IP)
    # test = {"0.0.0.0/0":{"username":"netdiscover","password":"password"}}
    request.session['devices_dict'] = str(deviceDiscovery(seed_IP, auth_dict))

    return HttpResponse("", content_type='text/plain')