@echo off
setlocal enabledelayedexpansion
set /p phoneNumber=phoneNumber: 
set /p bidType=bidType: 
set /p hostID=1-prod, 2-test: 
if %hostid% == 1 (
	set "PROD_HOST"
	) else (
		set "TEST_HOST"
		)
set "input_file=data.json"
set "output_file=temp.json"
for /f "tokens=*" %%a in (%input_file%) do (
    set "line=%%a"
    set "line=!line:"=!"    
    echo !line! | findstr "phoneNumber" > nul
    if errorlevel 1 (
        echo !line! | findstr "bidType" > nul
        if errorlevel 1 (
			echo !line! | findstr "{" > nul
			if errorlevel 1 (
				echo !line! | findstr "}" > nul
				if errorlevel 1 (
					echo     %%a>> %output_file%
				) else ( 
					echo !line!>> %output_file%
				)
			) else ( 
				echo !line!>> %output_file%
			)
        ) else (
			echo     ,"bidType": %bidType%>> %output_file%
			)
	) else (
		echo     "phoneNumber": "%phoneNumber%">> %output_file%
		)
)
@move /y %output_file% %input_file%	> nul
@type data.json | curl -X POST  http://%host%/api/STS/GetCodeNumber -H @headers.txt --data-binary @-
pause