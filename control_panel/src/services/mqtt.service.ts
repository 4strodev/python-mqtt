declare let Paho: any;

export class MqttService {
    client: any;
    connected: boolean = false;
    constructor(host: string, port: number, clientId: string) {
        this.client = new Paho.MQTT.Client(host, port, clientId);
    }

    onMessage(callback: (message: any) => void) {
        this.client.onMessageArrived = callback;
    }

    async connect() {

        return new Promise<void>((resolve, reject) => {
            const onSuccess = () => {
                this.connected = true;
                resolve();
            }

            this.client.connect({
                timeout: 3,
                cleanSession: true,
                onSuccess,
                onFailure: reject
            });
        });
    }

    subscribe(topic: string) {
        if (!this.connected) {
            throw new Error("Client not connected");
        }
        this.client.subscribe(topic);
    }
}
