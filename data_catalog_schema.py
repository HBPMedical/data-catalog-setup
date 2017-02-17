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

    unique_constraint = UniqueConstraint(
        dataset, matlab_version, spm_version, spm_revision, fn_called, fn_version, others)


class ProcessingStep(Base):
    __tablename__ = 'processing_step'

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(200), nullable=False)
    provenance_id = Column(ForeignKey('provenance.id'), nullable=False)
    previous_step_id = Column(ForeignKey('processing_step.id'))
    execution_date = Column(DATE)

    unique_constraint = UniqueConstraint(name, provenance_id)

    provenance = relationship('Provenance')
    processing_step = relationship('ProcessingStep')


class DataFile(Base):
    __tablename__ = 'data_file'

    id = Column(INTEGER, primary_key=True)
    path = Column(TEXT, unique=True, nullable=False)
    type = Column(VARCHAR(50), nullable=False)
    processing_step_id = Column(ForeignKey('processing_step.id'), nullable=False)
    repetition_id = Column(ForeignKey('repetition.id'))
    is_copy = Column(Boolean)

    processing_step = relationship('ProcessingStep')
    repetition = relationship('Repetition')


class Repetition(Base):
    __tablename__ = 'repetition'

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    sequence_id = Column(ForeignKey('sequence.id'), nullable=False)
    date = Column(DATE)

    unique_constraint = UniqueConstraint(name, sequence_id)

    sequence = relationship('Sequence')


class Sequence(Base):
    __tablename__ = 'sequence'

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    session_id = Column(ForeignKey('session.id'), nullable=False)
    sequence_type_id = Column(ForeignKey('sequence_type.id'))

    unique_constraint = UniqueConstraint(name, session_id)

    sequence_type = relationship('SequenceType')
    session = relationship('Session')


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
    name = Column(VARCHAR(50), nullable=False)
    visit_id = Column(ForeignKey('visit.id'), nullable=False)
    date = Column(DATE)

    unique_constraint = UniqueConstraint(name, visit_id)

    visit = relationship('Visit')


class Visit(Base):
    __tablename__ = 'visit'

    id = Column(INTEGER, primary_key=True, autoincrement=False)
    date = Column(DATE)
    role = Column(Enum('C', 'P', 'IC', name='participant_role'))
    comment = Column(TEXT)
    participant_id = Column(ForeignKey('participant.id'), nullable=False)

    participant = relationship('Participant')


class Participant(Base):
    __tablename__ = 'participant'

    id = Column(INTEGER, primary_key=True, autoincrement=False)
    gender = Column(Enum('M', 'F', 'O', name='gender'))
    birth_date = Column(DATE)
    age = Column(DECIMAL)


class VisitMapping(Base):
    __tablename__ = 'visit_mapping'

    name = Column(VARCHAR(50), primary_key=True)
    dataset = Column(VARCHAR(50), primary_key=True)
    visit_id = Column(INTEGER, unique=True)


class ParticipantMapping(Base):
    __tablename__ = 'participant_mapping'

    name = Column(VARCHAR(50), primary_key=True)
    dataset = Column(VARCHAR(50), primary_key=True)
    participant_id = Column(INTEGER, unique=True)
