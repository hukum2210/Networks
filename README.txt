SIMPLE ANNA UNIVERSITY CN PRACTICAL CODE PACK

8 topics, each with server.py, client.py and simpy_code.py:
TCP Chat, UDP Chat, Multi-Client Chat, ARP, Go-Back-N, Selective Repeat,
CSMA, Packet Routing.

Run server.py first, then client.py in a second terminal in the same topic folder.
Run SimPy examples separately. Install SimPy once with:
    python -m pip install simpy

All Python files avoid comments/docstrings and use short, basic code.
These are simplified learning examples. Some transport/socket examples are
minimal demonstrations and do not implement every protocol detail or robust
framing/retransmission. ARP uses a simulated lookup table, and routing uses a
small graph with shortest-path calculation.
