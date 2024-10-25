from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.gator import Gator
import pandas as pd
from typing import List
from schemas.gator import GatorSchema

def sanitize_column_name(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('#','number').str.replace('-','_').str.replace('.','').str.lower()
    return df
    
def sanitize_dataframe(df):
    # Replace NaN with None to handle SQL null values
    df = df.replace({float('nan'): None, 'nan': None, pd.NA: None, None: None})
    # You can apply further column sanitization here if needed
    return df


router = APIRouter()

@router.get("/", response_model=List[GatorSchema])
def get_all_gator(skip: int =0, db:Session = Depends(get_db)):
    gators = db.query(Gator).all()
    return gators

@router.get("/{gator_id}", response_model=GatorSchema)
def get_gator(gator_id: int, db: Session = Depends(get_db)):
    gator = db.query(Gator).filter(Gator.id == gator_id).first()
    if gator is None:
        raise HTTPException(status_code=404, detail="Gator ID not Found")
    else:
        return gator

# Not Working Yet....
@router.get('/title/{title_desc}', response_model=List[GatorSchema])
def search_gator_by_title(title_desc: str, db: Session = Depends(get_db)):
    gator_records = db.query(Gator).filter(Gator.title_desc.ilike(f"%{title_desc}%")).all()
    if gator_records:
        return gator_records
    else:
        raise HTTPException(status_code=404, detail="No Records Found with given title")

@router.post("/upload")
async def upload_file(file:UploadFile=File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    df = pd.read_excel(contents)
    df = sanitize_column_name(df)
    df = sanitize_dataframe(df)
    
    for _, row in df.iterrows():
        new_entry = Gator(
            wb_id = row.get('wb_id'),
            barcode = row.get('barcode'),
            title_no = row.get('title_no'),
            title_desc = row.get('title_desc'),
            mpm_number = row.get('mpm_number'),
            ep_title = row.get('ep_title'),
            episode_number = row.get('episode_number'),
            med_fmt = row.get('med_fmt'),
            element = row.get('elememt'),
            size = row.get('size'),
            standard = row.get('standard'),
            localized = row.get('localized'),
            language_1 = row.get('language_1'),
            language_2 = row.get('language_2'),
            langauge_3 = row.get('language_3'),
            langauge_4  = row.get('language_4'),
            content = row.get('content'),
            audio_mix = row.get('audio_mix'),
            audio_format = row.get('audio_format'),
            audio_appl = row.get('audio_appl'),
            asset_desc = row.get('asset_desc'),
            track_config = row.get('track_config'),
            film_aspect = row.get('film_aspect'),
            audio_bit_rate = row.get('audio_bit_rate'),
            video_aspect = row.get('video_aspect'),
            text = row.get('text'),
            music_effects = row.get('music_effects'),
            version = row.get('version'),
            file_type = row.get('file_type'),
            container = row.get('container'),
            container_1 = row.get('container_1'),
            container_2 = row.get('container_2'),
            category = row.get('category'),
            title_option = row.get('title_option'),
            asset_type = row.get('asset_type'),
            status = row.get('status'),
            active = row.get('active'),
            being_made_by = row.get('being_made_by'),
            current_facility = row.get('current_facility'),
            home_facility = row.get('home_facility'),
            library = row.get('library'),
            material = row.get('material'),
            process = row.get('process'),
            set_length = row.get('set_length'),
            no_of_units = row.get('no_of_units'),
            shelf = row.get('shelf'),
            reel_notes = row.get('reel_notes'),
            reel_tag = row.get('reel_tag'),
            frame_rate = row.get('frame_rate'),
            rating = row.get('rating'),
            coloring = row.get('coloring'),
            stock_material = row.get('stock_material'),
            create_date = row.get('create_date'),
            gator_mpm_number = row.get('gator_mpm_number'), # Changed # to "number"
            movement_reserved = row.get('movement_reserved'),
            qc_status = row.get('qc_status'),
            condition = row.get('condition'),
            print_number = row.get('print_number'), # Changed # to "number"
            inv_type = row.get('inv_type'),
            asset_note = row.get('asset_note'),
            sync_system = row.get('sync_system'),
            container_wb_id = row.get('container_wb_id'),
            container_barcode = row.get('containter_barcode'),
            reserved = row.get('reserved'),
            asset_set_id = row.get('asset_set_id'),
            set_no = row.get('set_no'),
            set_total = row.get('set_total'),
            part_asset_no = row.get('part_asset_no'),
            run_time = row.get('run_time'),
            owner = row.get('owner'),
            alert_not_no_text = row.get('alert_not_no_text'),
            title_in_package = row.get('title_in_package'),
            title_type = row.get('title_type'),
            story_time = row.get('story_time'),
            track_assign = row.get('track_assign'),
            title_version = row.get('title_version'),
            title_no_episodic_mpm = row.get('title_no_episodic_mpm'), ## NEED CHECK
            localization = row.get('localization'),
            enviroment = row.get('enviroment'),
            vault = row.get('valut'),
            user_added = row.get('user_added'),
            user_changed = row.get('user_changed'),
            original_system = row.get('original_system'),
        )
        db.add(new_entry)
    db.commit()
    return {'message': "File processed successfully"}        

