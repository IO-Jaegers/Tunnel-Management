# iptables -A FORWARD -i main-network -j ACCEPT; iptables -t nat -A POSTROUTING -o eno1 -j MASQUERADE; iptables -t nat -A POSTROUTING -o wlo2 -j MASQUERADE;
#  iptables -D FORWARD -i main-network -j ACCEPT; iptables -t nat -D POSTROUTING -o eno1 -j MASQUERADE; iptables -t nat -A POSTROUTING -o wlo2 -j MASQUERADE
