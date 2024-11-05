class MonHoc:
    current_id=100
    def __init__(self,ten_mh, tong_so_tiet, loai_mon) :
        self.ma_mon_hoc=MonHoc.current_id
        MonHoc.current_id+=1
        self.ten_mh=ten_mh
        self.tong_so_tiet=tong_so_tiet
        self.loai_mon=loai_mon
    def to_string(self):
        return f"{self.ma_mon_hoc},{self.ten_mh},{self.tong_so_tiet},{self.loai_mon}"
    @staticmethod
    def from_string(data):
        ma_mon_hoc,ten_mon,tong_so_tiet,loai_mon=data.split(",")
        obj=MonHoc(ten_mon,int(tong_so_tiet),loai_mon)
        obj.ma_mon_hoc=int(ma_mon_hoc)
        return obj
    @classmethod
    def them_mon_hoc(cls,filename):
        ds_mon_hoc=cls.load_to_file(filename)
        ten_mon=input()
        tong_so_tiet=int(input())
        loai_mon=input()
        mon_hoc=cls(ten_mon,tong_so_tiet,loai_mon)
        ds_mon_hoc.append(mon_hoc)
        cls.save_to_file(filename,ds_mon_hoc)
        print("Danh sach mon hoc:")
        for mon in ds_mon_hoc:
            print(f"Mã môn: {mon.ma_mon_hoc}, Tên môn: {mon.ten_mon}, Loại môn: {mon.loai_mon}")
    @staticmethod
    def save_to_file(filename,data):
        with open(filename,'w',encoding='utf-8') as f:
            for obj in data:
                f.write(obj.to_string()+"\n")



    @staticmethod
    def load_to_file(filename):
        try:
            with open(filename,'r',encoding='utf-8') as f:
                data=f.readline()
                return [MonHoc.from_string(item.strip()) for item in data]
        except FileExistsError:
            return []
class GiangVien:
    current_id=100
    def __init__(self,ten_mh, tong_so_tiet, loai_mon) :
        self.ma_mon_hoc=MonHoc.current_id
        MonHoc.current_id+=1
        self.ten_mh=ten_mh
        self.tong_so_tiet=tong_so_tiet
        self.loai_mon=loai_mon
    def to_string(self):
        return f"{self.ma_mon_hoc},{self.ten_mh},{self.tong_so_tiet},{self.loai_mon}"
    @staticmethod
    def from_string(data):
        ma_mon_hoc,ten_mon,tong_so_tiet,loai_mon=data.split(",")
        obj=MonHoc(ten_mon,int(tong_so_tiet),loai_mon)
        obj.ma_mon_hoc=int(ma_mon_hoc)
        return obj
    @classmethod
    def them_mon_hoc(cls,filename):
        ds_mon_hoc=cls.load_to_file(filename)
        ten_mon=input()
        tong_so_tiet=int(input())
        loai_mon=input()
        mon_hoc=cls(ten_mon,tong_so_tiet,loai_mon)
        ds_mon_hoc.append(mon_hoc)
        cls.save_to_file(filename,ds_mon_hoc)
        print("Danh sach mon hoc:")
        for mon in ds_mon_hoc:
            print(f"Mã môn: {mon.ma_mon_hoc}, Tên môn: {mon.ten_mon}, Loại môn: {mon.loai_mon}")
    @staticmethod
    def save_to_file(filename,data):
        with open(filename,'w',encoding='utf-8') as f:
            for obj in data:
                f.write(obj.to_string()+"\n")



    @staticmethod
    def load_to_file(filename):
        try:
            with open(filename,'r',encoding='utf-8') as f:
                data=f.readline()
                return [MonHoc.from_string(item.strip()) for item in data]
        except FileExistsError:
            return []