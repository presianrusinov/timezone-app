# timezone-app
A podman container which outputs your timezone in the browser, using Python code


Steps to run:
1.Pull the repo 
2. In a Linux environment enter the directory with the repo and execute the following commands (make sure you have podman installed first): podman build -t . podman run -p 8080:8080 
3. Enter your browser, type http://localhost:8080 , enter the timezone which you would like to get information for (use the syntax America/New_York or America/Los_Angeles with a underscore between the city's name for these type of cities)
4. Enjoy :)

"America/New_York" (Eastern Time)
"Europe/London" (Greenwich Mean Time)
"Asia/Tokyo" (Japan Standard Time)
"Africa/Cairo" (Eastern European Time)
"Asia/Shanghai" (China Standard Time)
"Australia/Sydney" (Australian Eastern Standard Time)
"Pacific/Honolulu" (Hawaii-Aleutian Standard Time)
"Indian/Maldives" (Maldives Time)
"Etc/GMT" (Coordinated Universal Time)

And more :)
