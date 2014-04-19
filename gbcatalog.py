import os,struct,zipfile

def getGBtype(rom_type):

    if (rom_type == 0x00):
        return "ROM"
    elif (rom_type == 0x08):
        return "ROM+RAM"
    elif (rom_type == 0x09):
        return "ROM+RAM+BATT"
    elif (rom_type == 0x01):
        return "MBC1"
    elif (rom_type == 0x02):
        return "MBC1+RAM"    
    elif (rom_type == 0x03):
        return "MBC1+RAM+BATT"
    elif (rom_type == 0x05):
        return "MBC2"
    elif (rom_type == 0x06):
        return "MBC2+BATT"
    elif (rom_type == 0x0F):
        return "MBC3+BATT+RTC"
    elif (rom_type == 0x10):
        return "MBC3+RAM+BATT+RTC"
    elif (rom_type == 0x11):
        return "MBC3"    
    elif (rom_type == 0x12):
        return "MBC3+RAM"
    elif (rom_type == 0x13):
        return "MBC3+RAM+BATT"    
    elif (rom_type == 0xFC):
        return "CAMERA"        
    elif (rom_type == 0x19):
        return "MBC5"
    elif (rom_type == 0x1A):
        return "MBC5+RAM"
    elif (rom_type == 0x1B):
        return "MBC5+RAM+BATT"
    elif (rom_type == 0x1C):
        return "MBC5+RUMBLE"    
    elif (rom_type == 0x1D):
        return "MBC5+RAM+RUMBLE"
    elif (rom_type == 0x1E):
        return "MBC5+RAM+BATT+RUMBLE"    
    elif (rom_type == 0x0B):
        return "MMMO1"        
    elif (rom_type == 0x0C):
        return "MMMO1+RAM"
    elif (rom_type == 0x0D):
        return "MMMO1+RAM+BATT"
    elif (rom_type == 0x15):
        return "MBC4"
    elif (rom_type == 0x16):
        return "MBC4+RAM"
    elif (rom_type == 0x17):
        return "MBC4+RAM+BATT"    
    elif (rom_type == 0x22):
        return "MBC7+RAM+BATT"
    elif (rom_type == 0x55):
        return "GG"    
    elif (rom_type == 0x56):
        return "GS3"    
    elif (rom_type == 0xFD):
        return "TAMA5"        
    elif (rom_type == 0xFF):
        return "HuC1"    
    elif (rom_type == 0xFE):
        return "HuC3"  
    else:
        return "??????"  
        

def getGBrom(rom_size):

    if (rom_size == 0x00):
        return "256Kb"
    elif (rom_size == 0x01):
        return "512Kb"
    elif (rom_size == 0x02):
        return "1Mb"
    elif (rom_size == 0x03):
        return "2Mb"
    elif (rom_size == 0x04):
        return "4Mb"
    elif (rom_size == 0x05):
        return "8Mb"
    elif (rom_size == 0x06):
        return "16Mb"
    elif (rom_size == 0x07):
        return "32Mb"
    elif (rom_size == 0x52):
        return "9Mb"
    elif (rom_size == 0x53):
        return "10Mb"
    elif (rom_size == 0x54):
        return "12Mb"
    else:
        return "??????"  
        
def getGBram(ram_size):

    if (ram_size == 0x00):
        return "NO"
    elif (ram_size == 0x01):
        return "16Kb"
    elif (ram_size == 0x02):
        return "64Kb"
    elif (ram_size == 0x03):
        return "256Kb"
    elif (ram_size == 0x04):
        return "1Mb"
    else:
        return "??????"

def getGBcolor(value):

    if (value == 0x80):
        return "YES"
    if (value == 0xC0):
        return "YES"
    else:
        return "NO"

def getGBsuper(value):

    if (value == 0x03):
        return "YES"
    else:
        return "NO"

def getGBcountry(value):

    if (value == 0x00):
        return "JAP"
    elif (value == 0x01):
        return "INT"
    else:
        return "???"

def getGBvalid(value):

    if (value == 0x00):
        return "YES"
    else:
        return "NO"

html_file = open("gbcatalog.htm", "w")
text_file = open("gbcatalog.txt", "w")

counter = 0
template = "{0:7}{1:110}{2:17}{3:9}{4:22}{5:11}{6:10}{7:10}{8:6}{9:6}{10:8}{11:9}\n"



  
html_head = '<html><head><link href="gbcatalog.css" rel="stylesheet" type="text/css"></head><body><div class="datagrid"><table><thead><tr><th>#</th><th>FILE</th><th>NAME</th><th>VERSION</th><th>TYPE</th><th>REAL SIZE</th><th>ROM SIZE</th><th>RAM SIZE</th><th>CGB</th><th>SGB</th><th>REGION</th><th>VALID</th></tr></thead><tbody>'
html_foot = '</tbody></table></div></body></html>'

html_file.write(html_head)

for r,d,f in os.walk("."):
    f.sort()
    for files in f:
        file_path = files.lower()
        if file_path.endswith(".gb") or file_path.endswith(".gbc") or file_path.endswith(".cgb") or file_path.endswith(".sgb") or file_path.endswith(".dmg") or file_path.endswith(".zip"):
            rom_path = os.path.join(r, files)
            print (files)

            if ((counter % 100) == 0):
                text_file.write("====== ============================================================================================================= ================ ======== ===================== ========== ========= ========= ===== ===== ======= ======\n")
                text_file.write(template.format("#", "FILE", "NAME", "VERSION", "TYPE", "REAL SIZE", "ROM SIZE", "RAM SIZE", "CGB", "SGB", "REGION", "VALID"))
                text_file.write("====== ============================================================================================================= ================ ======== ===================== ========== ========= ========= ===== ===== ======= ======\n")
            
            if file_path.endswith(".zip"):    
                zip_file = zipfile.ZipFile(files, "r")
                for rom_in_zip in zip_file.namelist():
                    rom = zip_file.read(rom_in_zip)
                    realsize = len(rom)
                    header = rom[:0x150]
                    break
            else:            
                rom_file = open(rom_path,"rb")
                header = rom_file.read(0x150)
                realsize = os.path.getsize(rom_path)
                rom_file.close()

            nothing = header[0:0x134]
            name = header[0x134:0x143]
            color = header[0x143:0x144]
            licensee_n = header[0x144:0x146]
            sgb = header[0x146:0x147]
            type = header[0x147:0x148]
            romsize = header[0x148:0x149]
            ramsize = header[0x149:0x14A]
            destination = header[0x14A:0x14B]
            licensee_o = header[0x14B:0x14C]
            version = header[0x14C:0x14D]
            complement = header[0x14D:0x14E]
            checksum = header[0x14E:0x150]

            (rom_name_b,) = struct.unpack('15s', name)
            rom_name = rom_name_b.decode("ascii", "ignore")
            rom_name = rom_name[:rom_name.find("\0")]
            
            new_rom_name = ''
            for c in rom_name:
                n = ord(c)
                if (n < 32) or (n > 126):
                    new_rom_name += ' '
                else:
                    new_rom_name += chr(n)
            rom_name = new_rom_name       
            
            (rom_color,) = struct.unpack('B', color)
            (rom_sgb,) = struct.unpack('B', sgb)
            (rom_type,) = struct.unpack('B', type)
            realsize = (realsize / 1024) * 8
            if (realsize >= 1024):
                rom_realsize = "%0.2f" % (realsize / 1024)
                rom_realsize += "Mb"
            else:
                rom_realsize = "%0.2f" % realsize
                rom_realsize += "Kb"
            (rom_romsize,) = struct.unpack('B', romsize)
            (rom_ramsize,) = struct.unpack('B', ramsize)
            (rom_destination,) = struct.unpack('B', destination)
            (rom_version,) = struct.unpack('B', version)

            rom_checksum = 0
            for header_byte in header[0x134:0x14E]:
                rom_checksum += header_byte
            rom_checksum = (rom_checksum + 25) & 0xFF

            counter+=1

            text_file.write(template.format(str(counter), str(files), rom_name, str(rom_version), getGBtype(rom_type), str(rom_realsize), getGBrom(rom_romsize), getGBram(rom_ramsize), getGBcolor(rom_color), getGBsuper(rom_sgb), getGBcountry(rom_destination), getGBvalid(rom_checksum)))


            if ((counter % 2) == 1):
                html_file.write("<tr>")
            else:
                html_file.write('<tr class="alt">')
            
            html_file.write("<td>" + str(counter) + "</td><td>" + str(files) + "</td><td>" + rom_name + "</td><td>" + str(rom_version) + "</td><td>" + getGBtype(rom_type) + "</td><td>" + str(rom_realsize) + "</td><td>" + getGBrom(rom_romsize) + "</td><td>" + getGBram(rom_ramsize) + "</td><td>" + getGBcolor(rom_color) + "</td><td>" + getGBsuper(rom_sgb) + "</td><td>" + getGBcountry(rom_destination) + "</td><td>" + getGBvalid(rom_checksum) + "</td></tr>")
           
html_file.write(html_foot)

text_file.close()  
html_file.close()  
