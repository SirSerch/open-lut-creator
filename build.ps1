try{
    pyinstaller --onefile --noconsole -i .\assets\images\icon.ico --add-binary "assets\ui\appUI.ui;." .\app.py
}catch{
    try{
        pip install pyinstaller
        pyinstaller --onefile --noconsole -i .\assets\images\icon.ico --add-binary "assets\ui\appUI.ui;." .\app.py
    }catch{
        Write-Host "ERROR-Cannot build the app, error"
    }
}