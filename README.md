# Air Quality Monitoring Starter Solution

### Download
- Clone this repo `git clone https://github.com/DigitalShoestringSolutions/AirQualityMonitoring -b feature/recipe`
- Open the downloaded folder `cd AirQualityMonitoring`

### Configure & Assemble
- Edit the config file to set machine name `nano Config/Sensing/main.py`
- Check the recipe contains the Modules you desire `nano recipe.txt`
- Assemble the Service Modules `Modules/Asssembly/get_modules.sh`
- Restart to apply the settings to the downloaded Service Modules

### Build & Run
- Build the docker containers `docker compose build`
- Start the docker containers `./start.sh`

### Usage
- View the dashboard: navigate to `localhost:3000` in a web browser
