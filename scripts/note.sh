# Configuration
  # Firewall Rules
iptables -A FORWARD -i main-network -j ACCEPT; iptables -t nat -A POSTROUTING -o eno1 -j MASQUERADE; iptables -t nat -A POSTROUTING -o wlo2 -j MASQUERADE;
iptables -D FORWARD -i main-network -j ACCEPT; iptables -t nat -D POSTROUTING -o eno1 -j MASQUERADE; iptables -t nat -A POSTROUTING -o wlo2 -j MASQUERADE


# Command line
  # Generate Keys
sudo cat /etc/wireguard/private.key | wg pubkey | sudo tee /etc/wireguard/public.key

# Startup on boot
sudo systemctl enable wg-quick@wg0.service

# Set User from commandline
sudo wg set wg0 peer PeURxj4Q75RaVhBKkRTpNsBPiPSGb5oQijgJsTa29hg= allowed-ips 10.8.0.2,fd0d:86fa:c3bc::2