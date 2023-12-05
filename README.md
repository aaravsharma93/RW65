# RW65

# API For Maintaining data from kiosk

## Updating And Running this project on server
* `cd ~/RW65/rw65`
* `git pull`
* `pm2 restart ecosystem.config.json`
* To check logs `pm2 monit`
### To Run Docker 
`docker run -d --name yardman-postgres -p 5432:5432 -v ~/RW65/postgres_data:/var/lib/postgresql/data -e POSTGRES_PASSWORD=yardman_pass -e POSTGRES_USER=yardman_admin -e POSTGRES_DB=yardman_db postgres:13-alpine`
