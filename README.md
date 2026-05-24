# Network Traffic Generator
**EN-US**
The Network Traffic Generator is a robust, easy-to-use, open-source and free tool that generates traffic data for a destination host.
Providing the hostname, or the destination IP of a host, the tool generates IP datagrams with random data, and sends to the destination.

**In initialization setup, the user can define aditional parameters, like:**
* Transport layer protocol: Choose between sending data via TCP or UDP;
* Port: Define a target port for the datagrams or set it to 0 to run a loop that scans all ports (1 to 65535);
* Packet size in bytes: Specify the packet size in bytes based on the maximum supported by the network (MTU). If unknown, set the value to 0 to use a default size of 1400 bytes, which is a safe value supported by most networks.
* Sending interval: Define the delay between each datagram in seconds. Set it to 0 for no interval.
**CAUTION**: Disabling the time interval may overload both your CPU and the destination host's CPU, leading to freezes or system crashes.
* Packet Count: Set a specific number of packets to be sent or set it to 0 to send packets indefinitely until interrupted (Control+C).
  
## WARNING
**This software is intended strictly for educational purposes or controlled testing.
Improper use of this tool may result in DoS/DDoS (Denial of Service) effects.**

[What is DoS/DDoS?](https://en.wikipedia.org/wiki/Denial-of-service_attack)

Licence: [MIT License](https://github.com/Bartzin55/Network-Traffic-Generator/blob/main/LICENSE)

---

**PT-BR**
O Network Traffic Generator é uma ferramenta robusta, fácil de usar, open-source e grátis, que gera tráfego de dados para um host de destino.
Fornecendo o hostname, ou o IP de destino de um host, a ferramenta gera datagramas IP com dados aleatórios, e os envia ao destino.

**No setup de inicialização, você pode definir parâmetros adicionais como:**
* Protocolo de transporte: O usuário pode definir se deseja enviar os dados utilizando TCP ou UDP;
* Porta: Defina a porta específica para o envio dos pacotes (ou defina como 0 para um um loop que escaneie todas as portas (1 a 65535));
* Tamanho em bytes do pacote: O usuário pode especificar o tamanho do pacote, em bytes, caso você tenha conhecimento do máximo suportado pela rede em que o tráfego vai passar (MTU). (Se você não ter esse conehcimento, deixe o valor como 0, e o pacote enviadoserá de 1400 bytes, que é um valor seguro suportado pela maior parte das redes).
* intervalo de tempo de envio: O usuário pode definir um intervalo de tempo de envio decada datagrama, em segundos. Ou pode definir como 0, para que não haja intervalo. CUIDADO: Não definir limite de tempo pode sobrecarregar o seu, e o processador do host de destino, causando travamentos ou até crashes.
* Quantidade de pacotes: O usuário pode definir uma quantidade de pacotes que serão enviados, ou pode não definir um limite, e os pacotes serem enviados indefinidamente até que o usuário pressione CONTROL+C.
  
## AVISO
**Esse software deve ser utilizado somente com fins educacionais, ou para testes controlados. Essa ferramente utilizada de maneira incorreta, pode causar um efeito de ataque DOS/DDOS.**

[O que é um DoS/DDoS?](https://pt.wikipedia.org/wiki/Ataque_de_nega%C3%A7%C3%A3o_de_servi%C3%A7o)

Licença: [MIT License](https://github.com/Bartzin55/Network-Traffic-Generator/blob/main/LICENSE)