# Simple load balancing
Questo progetto ha lo scopo di mostrare come utilizzare il load balancing con Nginx e Prometheus per raccogliere le metriche.

# Dipendenze
- Docker

# Struttura del Progetto
Il progetto è suddiviso in due cartelle:

single-server: contiene un singolo server che non utilizza il load balancing con Nginx.
mult-server: contiene più server che utilizzano il load balancing con Nginx.

Utilizzo
Per eseguire il progetto, clonare il repository e posizionarsi nella cartella del progetto:

bash
Copy code
git clone https://github.com/mariobenissimo/docker-nginx-prometheus-load-balancer.git
cd docker-nginx-prometheus-load-balancer
Per eseguire il singolo server senza load balancing, entrare nella cartella server ed eseguire il comando:

bash
Copy code
cd single-server
docker-compose up
Per eseguire il load balancing con Nginx, entrare nella cartella load-balanced-server ed eseguire il comando:

bash
Copy code
cd mult-server
docker-compose up
In entrambi i casi, Docker Compose creerà i container necessari e li avvierà.

Per accedere alle metriche raccolte da Prometheus, aprire un browser e digitare l'indirizzo http://localhost:9090.
Le richieste vengono fatte in auotmatico dai client, tuttavia è possibile digitare http://localhost:8080 per contattare il server nginx e incrementare il numero di richieste totali. 
