import dataloaderV2

def main():
    dow_jones_df = dataloaderV2.Data()
    
    dow_jones_df.data_transform()
    
    dow_jones_df.basic_eda()
    
    dow_jones_df.calculate_yearly_avg()
    
    dow_jones_df.show_yearly_avg()


if __name__ == '__main__':
    main()



#dataloaderV2.print__name__()
