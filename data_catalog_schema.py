# coding: utf-8
from sqlalchemy import Boolean
from sqlalchemy import Column, ForeignKey, Enum, UniqueConstraint, DATE, DECIMAL, INTEGER, VARCHAR, TEXT
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
    repetition_id = Column(ForeignKey('repetition.id'))
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

    id = Column(INTEGER, primary_key=True)
    number = Column(INTEGER, nullable=False)
    sequence_id = Column(ForeignKey('sequence.id'), nullable=False)
    date = Column(DATE)

    sequence = relationship('Sequence')
    unique_constraint = UniqueConstraint(number, sequence_id)


class Sequence(Base):
    __tablename__ = 'sequence'

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    session_id = Column(ForeignKey('session.id'), nullable=False)
    sequence_type_id = Column(ForeignKey('sequence_type.id'))

    sequence_type = relationship('SequenceType')
    session = relationship('Session')
    unique_constraint = UniqueConstraint(name, session_id)


class SequenceType(Base):
    __tablename__ = 'sequence_type'

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(200), nullable=False)
    manufacturer = Column(VARCHAR(200))
    manufacturer_model_name = Column(VARCHAR(200))
    institution_name = Column(VARCHAR(200))
    slice_thickness = Column(DECIMAL)
    repetition_time = Column(DECIMAL)
    echo_time = Column(DECIMAL)
    echo_number = Column(INTEGER)
    number_of_phase_encoding_steps = Column(INTEGER)
    percent_phase_field_of_view = Column(DECIMAL)
    pixel_bandwidth = Column(INTEGER)
    flip_angle = Column(DECIMAL)
    rows = Column(INTEGER)
    columns = Column(INTEGER)
    magnetic_field_strength = Column(DECIMAL)
    space_between_slices = Column(DECIMAL)
    echo_train_length = Column(INTEGER)
    percent_sampling = Column(DECIMAL)
    pixel_spacing_0 = Column(DECIMAL)
    pixel_spacing_1 = Column(DECIMAL)


class Session(Base):
    __tablename__ = 'session'

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(200), nullable=False)
    scan_id = Column(ForeignKey('scan.id'), nullable=False)
    date = Column(DATE)

    scan = relationship('Scan')
    unique_constraint = UniqueConstraint(name, scan_id)


class Scan(Base):
    __tablename__ = 'scan'

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(200), nullable=False)
    date = Column(DATE)
    role = Column(Enum('C', 'P', 'IC', name='scan_role'))
    comment = Column(TEXT)
    participant_id = Column(ForeignKey('participant.id'), nullable=False)
    provenance_id = Column(ForeignKey('provenance.id'), nullable=False)

    participant = relationship('Participant')
    provenance = relationship('Provenance')
    unique_constraint = UniqueConstraint(name, provenance_id)


class Participant(Base):
    __tablename__ = 'participant'

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(200), nullable=False)
    gender = Column(Enum('M', 'F', 'O', name='gender'))
    handedness = Column(Enum('left', 'right', 'ambidexter', name='handedness'))
    birthdate = Column(DATE)
    age = Column(DECIMAL)
    provenance_id = Column(ForeignKey('provenance.id'), nullable=False)

    provenance = relationship('Provenance')
    unique_constraint = UniqueConstraint(name, provenance_id)
