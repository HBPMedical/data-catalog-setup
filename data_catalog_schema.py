# coding: utf-8
from sqlalchemy import Boolean
from sqlalchemy import Column, Index, ForeignKey, Enum, DATE, DECIMAL, INTEGER, VARCHAR, TEXT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Provenance(Base):
    __tablename__ = 'provenance'

    id = Column(INTEGER, primary_key=True)
    dataset = Column(VARCHAR(50), nullable=False)
    matlab_version = Column(VARCHAR(50))
    spm_version = Column(VARCHAR(50))
    spm_revision = Column(VARCHAR(50))
    fn_called = Column(VARCHAR(50))
    fn_version = Column(VARCHAR(50))
    others = Column(TEXT)


class ProcessingStep(Base):
    __tablename__ = 'processing_step'

    id = Column(INTEGER, primary_key=True)
    previous_step_id = Column(ForeignKey('processing_step.id'))
    provenance_id = Column(ForeignKey('provenance.id'), nullable=False)
    name = Column(VARCHAR(200), nullable=False)
    execution_date = Column(DATE)

    processing_step = relationship('ProcessingStep')
    provenance = relationship('Provenance')


class DataFile(Base):
    __tablename__ = 'data_file'

    id = Column(INTEGER, primary_key=True)
    repetition_id = Column(ForeignKey('repetition.index_id'))
    processing_step_id = Column(ForeignKey('processing_step.id'), nullable=False)
    path = Column(TEXT, unique=True, nullable=False)
    type = Column(VARCHAR(50), nullable=False)
    result_type = Column(VARCHAR(50))
    output_type = Column(VARCHAR(50))
    is_copy = Column(Boolean)

    repetition = relationship('Repetition')
    processing_step = relationship('ProcessingStep')


class Repetition(Base):
    __tablename__ = 'repetition'

    name = Column(VARCHAR(50), primary_key=True)
    sequence_id = Column(ForeignKey('sequence.index_id'), primary_key=True)
    date = Column(DATE)
    index_id = Column(INTEGER, nullable=False, autoincrement=True, index=True, unique=True)

    sequence = relationship('Sequence')


class Sequence(Base):
    __tablename__ = 'sequence'

    name = Column(VARCHAR(50), primary_key=True)
    session_id = Column(ForeignKey('session.index_id'), primary_key=True)
    sequence_type_id = Column(ForeignKey('sequence_type.id'), nullable=False)
    index_id = Column(INTEGER, nullable=False, autoincrement=True, index=True, unique=True)

    sequence_type = relationship('SequenceType')
    session = relationship('Session')


class SequenceType(Base):
    __tablename__ = 'sequence_type'

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(200), nullable=False)
    manufacturer = Column(VARCHAR(200), nullable=True)
    manufacturer_model_name = Column(VARCHAR(200), nullable=True)
    institution_name = Column(VARCHAR(200), nullable=True)
    slice_thickness = Column(DECIMAL, nullable=True)
    repetition_time = Column(DECIMAL, nullable=True)
    echo_time = Column(DECIMAL, nullable=True)
    echo_number = Column(INTEGER, nullable=True)
    number_of_phase_encoding_steps = Column(INTEGER, nullable=True)
    percent_phase_field_of_view = Column(DECIMAL, nullable=True)
    pixel_bandwidth = Column(INTEGER, nullable=True)
    flip_angle = Column(DECIMAL, nullable=True)
    rows = Column(INTEGER, nullable=True)
    columns = Column(INTEGER, nullable=True)
    magnetic_field_strength = Column(DECIMAL, nullable=True)
    space_between_slices = Column(DECIMAL, nullable=True)
    echo_train_length = Column(INTEGER, nullable=True)
    percent_sampling = Column(DECIMAL, nullable=True)
    pixel_spacing_0 = Column(DECIMAL, nullable=True)
    pixel_spacing_1 = Column(DECIMAL, nullable=True)


class Session(Base):
    __tablename__ = 'session'

    name = Column(VARCHAR(200), primary_key=True)
    scan_id = Column(ForeignKey('scan.index_id'), primary_key=True)
    date = Column(DATE)
    index_id = Column(INTEGER, nullable=False, autoincrement=True, index=True, unique=True)

    scan = relationship('Scan')


class Scan(Base):
    __tablename__ = 'scan'

    id = Column(VARCHAR(200), primary_key=True)
    date = Column(DATE)
    role = Column(Enum('C', 'P', 'IC', 'U', name='scan_role'))
    comment = Column(TEXT)
    participant_id = Column(ForeignKey('participant.index_id'), nullable=False)
    provenance_id = Column(ForeignKey('provenance.id'), primary_key=True)
    index_id = Column(INTEGER, nullable=False, autoincrement=True, index=True, unique=True)

    participant = relationship('Participant')
    provenance = relationship('Provenance')


class Participant(Base):
    __tablename__ = 'participant'

    id = Column(VARCHAR(200), primary_key=True)
    gender = Column(Enum('male', 'female', 'other', 'unknown', name='gender'))
    handedness = Column(Enum('left', 'right', 'ambidexter', 'unknown', name='handedness'))
    birthdate = Column(DATE)
    age = Column(DECIMAL)
    provenance_id = Column(ForeignKey('provenance.id'), primary_key=True)
    index_id = Column(INTEGER, nullable=False, autoincrement=True, index=True, unique=True)

    provenance = relationship('Provenance')
