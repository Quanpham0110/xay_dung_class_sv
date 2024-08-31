class SinhVien:
    def __init__(self,id='',ten='',diem_toan=0,diem_van=0,diem_hoa=0) -> None:
        self.id:int=id
        self.ten:str=ten
        self.diem_toan:float=diem_toan
        self.diem_van:float=diem_van
        self.diem_hoa:float=diem_hoa
    
    def themSV(self):
        self.id=input('Nhập ID sinh viên: ')
        self.ten=input('Nhập tên sinh viên: ') 
        self.diem_toan=float(input('Nhập điểm toán: '))
        self.diem_van=float(input('Nhập điểm văn: '))
        self.diem_hoa=float(input('Nhập điểm hóa: '))

    def dtb(self):
        dtb=(self.diem_toan+self.diem_van+self.diem_hoa)//3
        return dtb        
    
    
    def show_SV(self):
        print(f'''
              ID sinh viên: {self.id}
              Tên sinh viên: {self.ten}
              Điểm toán: {self.diem_toan}
              Điểm văn: {self.diem_van}
              Điểm hóa: {self.diem_hoa}            
              Điểm trung bình: {self.dtb()}
              ''')
#============================================
class quanlySV:
    def __init__(self,) -> None:
        self.list_SV:list[SinhVien]=[]
    
    def add_SV(self,SV_moi:SinhVien):
        self.list_SV.append(SV_moi)
    
    def show_lst_SV_dtb_lon_hon_5(self):
        print('Danh sách những sinh viên có điểm trung bình > 5:')
        for sv in self.list_SV:
            if sv.dtb()>5:
                sv.show_SV()

    def show_lst_SV_hoa_nho_hon_5(self):
        print('danh sách sinh viên có điểm hóa < 5:')
        for sv in self.list_SV:
            if sv.diem_hoa <5:
                sv.show_SV()
#====================================
chay=True
qlsv=quanlySV()
while chay:
    print('''
        1) Thêm sinh viên
        2) Hiển thị sinh viên điểm tb>5
        3) Hiển thị sinh viên điểm hóa<5
        4) Thoát chương  trình
        ''')
    option=int(input('Nhập lựa chọn của bạn: '))
    if option==1:
        print('Thêm sinh viên mới')
        SV_moi=SinhVien()
        SV_moi.themSV()
        qlsv.add_SV(SV_moi)
    
    elif option ==2:
        qlsv.show_lst_SV_dtb_lon_hon_5()
    
    elif option ==3:
        qlsv.show_lst_SV_hoa_nho_hon_5()
    
    elif option ==4:
        chay=False    
    else:
        print('Cú pháp sai rồi ba,nhập lại đi!!!!!!!!')                
