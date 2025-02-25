from browser import document, window, html

def read_excel(event):
    file_input = document["fileInput"]
    file = file_input.files[0]
    reader = window.FileReader.new()
    
    def onload(event):
        data = event.target.result
        workbook = window.XLSX.read(data, {'type': 'binary'})
        first_sheet_name = workbook.SheetNames[0]
        sheet = workbook.Sheets[first_sheet_name]
        json_data = window.XLSX.utils.sheet_to_json(sheet)
        display_charts(json_data)
    
    reader.readAsBinaryString(file)
    reader.bind("load", onload)

def display_charts(data):
    charts_container = document["charts"]
    charts_container.clear()
    
    import matplotlib.pyplot as plt
    import io
    from base64 import b64encode

    for column in data[0]:
        values = [row[column] for row in data]
        plt.figure()
        plt.plot(values)
        plt.title(column)
        
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png')
        img_buffer.seek(0)
        img_data = b64encode(img_buffer.read()).decode('utf-8')
        
        img = html.IMG(src=f'data:image/png;base64,{img_data}')
        charts_container <= img

document["fileInput"].bind("change", read_excel)
