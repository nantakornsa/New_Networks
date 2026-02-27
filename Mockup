```mermaid
flowchart TB

    subgraph Edge Layer
        IoT1[IoT Sensor]
        IoT2[CCTV Camera]
        IoT3[Smart Device]
    end

    subgraph Connectivity Layer
        ISP[5G Network / ISP]
        Edge[Edge Gateway]
    end

    subgraph Cloud Layer
        LB[Load Balancer]
        APP[Application Server]
        DB[(Database)]
    end

    subgraph Security Layer
        FW[Firewall]
        VLAN[VLAN]
        SSL[SSL/TLS]
        ACL[ACL]
    end

    IoT1 --> Edge
    IoT2 --> Edge
    IoT3 --> Edge

    Edge --> ISP
    ISP --> LB
    LB --> APP
    APP --> DB

    APP --> FW --> VLAN --> SSL --> ACL
```
