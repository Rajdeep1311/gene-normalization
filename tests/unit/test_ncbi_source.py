"""Test import of NCBI source data"""
import pytest
from gene.schemas import Gene, MatchType, SourceName
from gene.query import QueryHandler
from datetime import datetime
from tests.conftest import assertion_checks, check_ncbi_discontinued_gene


@pytest.fixture(scope='module')
def ncbi():
    """Build ncbi test fixture."""
    class QueryGetter:
        def __init__(self):
            self.query_handler = QueryHandler()

        def search(self, query_str, incl='ncbi'):
            resp = self.query_handler.search(query_str, keyed=True, incl=incl)
            return resp['source_matches'][SourceName.NCBI]

    n = QueryGetter()
    return n


@pytest.fixture(scope='module')
def dpf1():
    """Create gene fixture for DPF1."""
    params = {
        'label': 'double PHD fingers 1',
        'concept_id': 'ncbigene:8193',
        'symbol': 'DPF1',
        'aliases': ['BAF45b', 'NEUD4', 'neuro-d4', 'SMARCG1'],
        'xrefs': ['hgnc:20225', 'ensembl:ENSG00000011332'],
        'previous_symbols': [],
        'associated_with': ['omim:601670'],
        'symbol_status': None,
        'location_annotations': [],
        'strand': '-',
        'locations': [
            {
                '_id': 'ga4gh:VCL.nEPKXzyfglrOMMFySOTQ8Om_f6xmr-pP',
                'chr': '19',
                'interval': {
                    'end': 'q13.2',
                    'start': 'q13.2',
                    'type': 'CytobandInterval'
                },
                'species_id': 'taxonomy:9606',
                'type': 'ChromosomeLocation'
            },
            {
                '_id': 'ga4gh:VSL.MbzGuoGI9MRB8oPe6eE-ULk3FIBdpMF8',
                'interval': {
                    'end': {'value': 38229695, 'type': 'Number'},
                    'start': {'value': 38211005, 'type': 'Number'},
                    'type': 'SequenceInterval'
                },
                'sequence_id': 'ga4gh:SQ.IIB53T8CNeJJdUqzn9V_JnRtQadwWCbl',
                'type': 'SequenceLocation'
            }
        ]
    }
    return Gene(**params)


@pytest.fixture(scope='module')
def pdp1():
    """Create gene fixture for PDP1."""
    params = {
        'label': 'pyruvate dehydrogenase phosphatase catalytic subunit 1',
        'concept_id': 'ncbigene:54704',
        'symbol': 'PDP1',
        'aliases': ['PDH', 'PDP', 'PDPC', 'PPM2A', 'PPM2C'],
        'xrefs': ['hgnc:9279', 'ensembl:ENSG00000164951'],
        'previous_symbols': ['LOC157663', 'PPM2C'],
        'associated_with': ['omim:605993'],
        'symbol_status': None,
        'location_annotations': [],
        'strand': '+',
        'locations': [
            {
                '_id': 'ga4gh:VCL.n9W_wjDCStQf29yPcjhkMnFmESG8wN9A',
                'chr': '8',
                'interval': {
                    'end': 'q22.1',
                    'start': 'q22.1',
                    'type': 'CytobandInterval'
                },
                'species_id': 'taxonomy:9606',
                'type': 'ChromosomeLocation'
            },
            {
                '_id': 'ga4gh:VSL.KmLM61Mm2jxuep7cdgg7lvOOXaIxSW0Y',
                'interval': {
                    'end': {'value': 93926068, 'type': 'Number'},
                    'start': {'value': 93916922, 'type': 'Number'},
                    'type': 'SequenceInterval'
                },
                'sequence_id': 'ga4gh:SQ.209Z7zJ-mFypBEWLk4rNC6S_OxY5p7bs',
                'type': 'SequenceLocation'
            }
        ]

    }
    return Gene(**params)


# X and Y chromosomes
@pytest.fixture(scope='module')
def spry3():
    """Create gene fixture for SPRY3."""
    params = {
        'label': 'sprouty RTK signaling antagonist 3',
        'concept_id': 'ncbigene:10251',
        'symbol': 'SPRY3',
        'aliases': ['spry-3'],
        'xrefs': ['hgnc:11271', 'ensembl:ENSG00000168939'],
        'previous_symbols': ['LOC170187', 'LOC253479'],
        'associated_with': ['omim:300531'],
        'symbol_status': None,
        'location_annotations': [],
        'strand': '+',
        'locations': [
            {
                '_id': 'ga4gh:VCL.A1s9hZY1tgmRi1WuXM1ETZOqJcpo4Ftx',
                'chr': 'Y',
                'interval': {
                    'end': 'q12',
                    'start': 'q12',
                    'type': 'CytobandInterval'
                },
                'species_id': 'taxonomy:9606',
                'type': 'ChromosomeLocation'
            },
            {
                '_id': 'ga4gh:VCL.fEBeCyej0jVKsvjw4vxyW6j1h8UVLb5S',
                'chr': 'X',
                'interval': {
                    'end': 'q28',
                    'start': 'q28',
                    'type': 'CytobandInterval'
                },
                'species_id': 'taxonomy:9606',
                'type': 'ChromosomeLocation'
            },
            {
                '_id': 'ga4gh:VSL.r6_z0hmAdPdufX0g1ciRj_zPU6poQviA',
                'interval': {
                    'end': {'value': 155782459, 'type': 'Number'},
                    'start': {'value': 155612585, 'type': 'Number'},
                    'type': 'SequenceInterval'
                },
                'sequence_id': 'ga4gh:SQ.w0WZEvgJF0zf_P4yyTzjjv9oW1z61HHP',
                'type': 'SequenceLocation'
            },
            {
                '_id': 'ga4gh:VSL.Cr_HtUTpUe6KB37Y7zOTDbx9JglIzE1O',
                'interval': {
                    'end': {'value': 56968979, 'type': 'Number'},
                    'start': {'value': 56923422, 'type': 'Number'},
                    'type': 'SequenceInterval'
                },
                'sequence_id': 'ga4gh:SQ.8_liLu1aycC0tPQPFmUaGXJLDs5SbPZ5',
                'type': 'SequenceLocation'
            }
        ]
    }
    return Gene(**params)


# chromosome but no map locations
@pytest.fixture(scope='module')
def adcp1():
    """Create gene fixture for ADCP1."""
    params = {
        'label': 'adenosine deaminase complexing protein 1',
        'concept_id': 'ncbigene:106',
        'symbol': 'ADCP1',
        'aliases': [],
        'xrefs': ['hgnc:229'],
        'previous_symbols': [],
        'associated_with': [],
        'symbol_status': None,
        'strand': None,
        'location_annotations': ['6'],
        'locations': []
    }
    return Gene(**params)


# no chromosome or map locations
@pytest.fixture(scope='module')
def afa():
    """Create gene fixture for AFA."""
    params = {
        'label': 'ankyloblepharon filiforme adnatum',
        'concept_id': 'ncbigene:170',
        'symbol': 'AFA',
        'aliases': [],
        'xrefs': [],
        'previous_symbols': [],
        'associated_with': ['omim:106250'],
        'symbol_status': None,
        'strand': None,
        'location_annotations': [],
        'locations': []
    }
    return Gene(**params)


# Contains non cytogenic locations (i.e. "map from Rosati....")
@pytest.fixture(scope='module')
def znf84():
    """Create gene fixture for ZNF84."""
    params = {
        'label': 'zinc finger protein 84',
        'concept_id': 'ncbigene:7637',
        'symbol': 'ZNF84',
        'aliases': ['HPF2'],
        'xrefs': ['hgnc:13159', 'ensembl:ENSG00000198040'],
        'previous_symbols': ["LOC100287429"],
        'associated_with': ['omim:618554'],
        'symbol_status': None,
        'location_annotations': ['map from Rosati ref via FISH [AFS]'],
        'strand': '+',
        'locations': [
            {
                '_id': 'ga4gh:VCL.CusjBE-q66vf4v8VSHRhMxjR_4G688Ve',
                'chr': '12',
                'interval': {
                    'end': 'q24.33',
                    'start': 'q24.33',
                    'type': 'CytobandInterval'
                },
                'species_id': 'taxonomy:9606',
                'type': 'ChromosomeLocation'
            },
            {
                '_id': 'ga4gh:VSL.w5FE3al-0SUkARxk_RdCD5ypYIh_WtSM',
                'interval': {
                    'end': {'value': 133063299, 'type': 'Number'},
                    'start': {'value': 133037300, 'type': 'Number'},
                    'type': 'SequenceInterval'
                },
                'sequence_id': 'ga4gh:SQ.6wlJpONE3oNb4D69ULmEXhqyDZ4vwNfl',
                'type': 'SequenceLocation'
            }
        ]
    }
    return Gene(**params)


# No arm or sub band
@pytest.fixture(scope='module')
def slc25a6():
    """Create gene fixture for SLC25A6."""
    params = {
        'label': 'solute carrier family 25 member 6',
        'concept_id': 'ncbigene:293',
        'symbol': 'SLC25A6',
        'aliases': ['AAC3', 'ANT', 'ANT 2', 'ANT 3', 'ANT3', 'ANT3Y'],
        'xrefs': ['hgnc:10992', 'ensembl:ENSG00000169100'],
        'previous_symbols': ["ANT3Y"],
        'associated_with': ['omim:300151', 'omim:403000'],
        'symbol_status': None,
        'location_annotations': ['X', 'Y'],
        'strand': '-',
        'locations': [
            {
                '_id': 'ga4gh:VSL.HG0bXHwmZoxZzU2ckz4T6lvxIswXhLQZ',
                'interval': {
                    'end': {'value': 1392113, 'type': 'Number'},
                    'start': {'value': 1386151, 'type': 'Number'},
                    'type': 'SequenceInterval'
                },
                'sequence_id': 'ga4gh:SQ.w0WZEvgJF0zf_P4yyTzjjv9oW1z61HHP',
                'type': 'SequenceLocation'
            },
            {
                '_id': 'ga4gh:VSL.1J-MNAWJ9hvZtIM_90lqLbxEt707zL_A',
                'interval': {
                    'end': {'value': 1392113, 'type': 'Number'},
                    'start': {'value': 1386151, 'type': 'Number'},
                    'type': 'SequenceInterval'
                },
                'sequence_id': 'ga4gh:SQ.8_liLu1aycC0tPQPFmUaGXJLDs5SbPZ5',
                'type': 'SequenceLocation'
            }
        ]
    }
    return Gene(**params)


# Contains arm but no sub band
@pytest.fixture(scope='module')
def loc106783576():
    """Create gene fixture for ."""
    params = {
        'label': 'nonconserved acetylation island sequence 68 enhancer',
        'concept_id': 'ncbigene:106783576',
        'symbol': 'LOC106783576',
        'aliases': [],
        'xrefs': [],
        'previous_symbols': [],
        'associated_with': [],
        'symbol_status': None,
        'location_annotations': [],
        'strand': None,
        'locations': [
            {
                '_id': 'ga4gh:VCL.RFN35KQMhqzhmo4QP7AxKAzlPtnh7slL',
                'chr': '10',
                'interval': {
                    'end': 'cen',
                    'start': 'pter',
                    'type': 'CytobandInterval'
                },
                'species_id': 'taxonomy:9606',
                'type': 'ChromosomeLocation'
            }
        ]
    }
    return Gene(**params)


# Testing for cen
@pytest.fixture(scope='module')
def glc1b():
    """Create gene fixture for GLC1B."""
    params = {
        'label': 'glaucoma 1, open angle, B (adult-onset)',
        'concept_id': 'ncbigene:2722',
        'symbol': 'GLC1B',
        'aliases': [],
        'xrefs': [],
        'previous_symbols': [],
        'associated_with': ['omim:606689'],
        'symbol_status': None,
        'location_annotations': [],
        'strand': None,
        'locations': [
            {
                '_id': 'ga4gh:VCL.HStPIl_6UkNQmbjZW1TeUmHFMptbIj6t',
                'chr': '2',
                'interval': {
                    'end': 'q13',
                    'start': 'cen',
                    'type': 'CytobandInterval'
                },
                'species_id': 'taxonomy:9606',
                'type': 'ChromosomeLocation'
            }
        ]
    }
    return Gene(**params)


# Testing for ter ranges
@pytest.fixture(scope='module')
def hdpa():
    """Create gene fixture for HDPA."""
    params = {
        'label': 'Hodgkin disease, susceptibility, pseudoautosomal',
        'concept_id': 'ncbigene:50829',
        'symbol': 'HDPA',
        'aliases': [],
        'xrefs': [],
        'previous_symbols': [],
        'associated_with': ['omim:300221'],
        'symbol_status': None,
        'location_annotations': [],
        'strand': None,
        'locations': [
            {
                '_id': 'ga4gh:VCL.faRHNO_VJMssbjYQ628mfdRgLqg9qK2b',
                'chr': 'X',
                'interval': {
                    'end': 'p22.32',
                    'start': 'pter',
                    'type': 'CytobandInterval'
                },
                'species_id': 'taxonomy:9606',
                'type': 'ChromosomeLocation'
            }
        ]
    }
    return Gene(**params)


# Testing for annotation
@pytest.fixture(scope='module')
def prkrap1():
    """Create gene fixture for PRKRAP1."""
    params = {
        'label': 'protein activator of interferon induced protein kinase '
                 'EIF2AK2 pseudogene 1',
        'concept_id': 'ncbigene:731716',
        'symbol': 'PRKRAP1',
        'aliases': [],
        'xrefs': ['hgnc:33447'],
        'previous_symbols': ['LOC100289695'],
        'associated_with': [],
        'symbol_status': None,
        'location_annotations': ['alternate reference locus'],
        'strand': '+',
        'locations': [
            {
                '_id': 'ga4gh:VCL.HeTd-jABCr22v4rUfVWJbkz2NkPyGScK',
                'chr': '6',
                'interval': {
                    'end': 'p21.3',
                    'start': 'p21.3',
                    'type': 'CytobandInterval'
                },
                'species_id': 'taxonomy:9606',
                'type': 'ChromosomeLocation'
            },
            {
                '_id': 'ga4gh:VSL.WB_2IFcms7VmbkPBXUgUaH-R1EdKRs4s',
                'interval': {
                    'end': {'value': 3941874, 'type': 'Number'},
                    'start': {'value': 3940269, 'type': 'Number'},
                    'type': 'SequenceInterval'
                },
                'sequence_id': 'ga4gh:SQ.MjujHSAsgNWRTX4w3ysM7b5OVhZpdXu1',
                'type': 'SequenceLocation'
            },
            {
                '_id': 'ga4gh:VSL.PIeADExe9_iSJkTLQbSvhxAJ8PM19R6r',
                'interval': {
                    'end': {'value': 3932085, 'type': 'Number'},
                    'start': {'value': 3930480, 'type': 'Number'},
                    'type': 'SequenceInterval'
                },
                'sequence_id': 'ga4gh:SQ.Q8IworEhpLeXwpz1CHM7C3luysh-ltx-',
                'type': 'SequenceLocation'
            }
        ]
    }
    return Gene(**params)


# start > end
@pytest.fixture(scope='module')
def mhb():
    """Create gene fixture for MHB."""
    params = {
        'label': 'myopathy, hyaline body, autosomal recessive',
        'concept_id': 'ncbigene:619511',
        'symbol': 'MHB',
        'aliases': [],
        'xrefs': [],
        'previous_symbols': [],
        'associated_with': ['omim:255160'],
        'symbol_status': None,
        'location_annotations': [],
        'strand': None,
        'locations': [
            {
                '_id': 'ga4gh:VCL.2WDJu032Gc_9BN4qiNELb577XomiZv8z',
                'chr': '3',
                'interval': {
                    'end': 'p21.32',
                    'start': 'p22.2',
                    'type': 'CytobandInterval'
                },
                'species_id': 'taxonomy:9606',
                'type': 'ChromosomeLocation'
            }
        ]
    }
    return Gene(**params)


# Different arms
@pytest.fixture(scope='module')
def spg37():
    """Create gene fixture for SPG37."""
    params = {
        'label': 'spastic paraplegia 37 (autosomal dominant)',
        'concept_id': 'ncbigene:100049159',
        'symbol': 'SPG37',
        'aliases': [],
        'xrefs': [],
        'previous_symbols': [],
        'associated_with': ['omim:611945'],
        'symbol_status': None,
        'location_annotations': [],
        'strand': None,
        'locations': [
            {
                '_id': 'ga4gh:VCL.P5jAIluXneqHZMV9FBEQ2ZqOpO-8fqbP',
                'chr': '8',
                'interval': {
                    'end': 'q13.3',
                    'start': 'p21.2',
                    'type': 'CytobandInterval'
                },
                'species_id': 'taxonomy:9606',
                'type': 'ChromosomeLocation'
            }
        ]
    }
    return Gene(**params)


def test_dpf1(ncbi, dpf1):
    """Test that DPF1 normalizes to correct gene concept."""
    # Concept ID
    normalizer_response = ncbi.search('ncbigene:8193')
    assertion_checks(normalizer_response, dpf1, 1, MatchType.CONCEPT_ID)

    normalizer_response = ncbi.search('ncbIgene:8193')
    assertion_checks(normalizer_response, dpf1, 1, MatchType.CONCEPT_ID)

    # Symbol
    normalizer_response = ncbi.search('DPF1')
    assertion_checks(normalizer_response, dpf1, 1, MatchType.SYMBOL)

    normalizer_response = ncbi.search('DpF1')
    assertion_checks(normalizer_response, dpf1, 1, MatchType.SYMBOL)

    # Alias
    normalizer_response = ncbi.search('BAF45b')
    assertion_checks(normalizer_response, dpf1, 1, MatchType.ALIAS)

    normalizer_response = ncbi.search('NEUD4')
    assertion_checks(normalizer_response, dpf1, 1, MatchType.ALIAS)

    normalizer_response = ncbi.search('neuro-d4')
    assertion_checks(normalizer_response, dpf1, 1, MatchType.ALIAS)

    # associated_with
    normalizer_response = ncbi.search('omim:601670')
    assertion_checks(normalizer_response, dpf1, 1, MatchType.ASSOCIATED_WITH)

    # No Match
    normalizer_response = ncbi.search('DPF 1')
    assert normalizer_response['match_type'] == 0

    normalizer_response = ncbi.search('DPG1')
    assert normalizer_response['match_type'] == 0


def test_pdp1(ncbi, pdp1):
    """Test that PDP1 normalizes to correct gene concept."""
    # Concept ID
    normalizer_response = ncbi.search('ncbigene:54704')
    assertion_checks(normalizer_response, pdp1, 1, MatchType.CONCEPT_ID)

    normalizer_response = ncbi.search('NCBIGENE:54704')
    assertion_checks(normalizer_response, pdp1, 1, MatchType.CONCEPT_ID)

    # Symbol
    normalizer_response = ncbi.search('PDP1')
    assertion_checks(normalizer_response, pdp1, 1, MatchType.SYMBOL)

    normalizer_response = ncbi.search('pdp1')
    assertion_checks(normalizer_response, pdp1, 1, MatchType.SYMBOL)

    # Previous Symbol
    normalizer_response = ncbi.search('LOC157663')
    assertion_checks(normalizer_response, pdp1, 1, MatchType.PREV_SYMBOL)

    normalizer_response = ncbi.search('PPM2C')
    assertion_checks(normalizer_response, pdp1, 1, MatchType.PREV_SYMBOL)

    normalizer_response = ncbi.search('loc157663')
    assertion_checks(normalizer_response, pdp1, 1, MatchType.PREV_SYMBOL)

    # Alias
    normalizer_response = ncbi.search('pdh')
    assertion_checks(normalizer_response, pdp1, 1, MatchType.ALIAS)

    normalizer_response = ncbi.search('PDP')
    assertion_checks(normalizer_response, pdp1, 1, MatchType.ALIAS)

    normalizer_response = ncbi.search('PDPC')
    assertion_checks(normalizer_response, pdp1, 1, MatchType.ALIAS)

    normalizer_response = ncbi.search('PPM2A')
    assertion_checks(normalizer_response, pdp1, 1, MatchType.ALIAS)


def test_spry3(ncbi, spry3):
    """Test that SPRY3 normalizes to correct gene concept."""
    # Concept ID
    normalizer_response = ncbi.search('NCBIgene:10251')
    assertion_checks(normalizer_response, spry3, 1, MatchType.CONCEPT_ID)

    # Symbol
    normalizer_response = ncbi.search('sprY3')
    assertion_checks(normalizer_response, spry3, 1, MatchType.SYMBOL)

    # Alias
    normalizer_response = ncbi.search('SPRY-3')
    assertion_checks(normalizer_response, spry3, 1, MatchType.ALIAS)


def test_adcp1(ncbi, adcp1):
    """Test that ADCP1 normalizes to correct gene concept."""
    # Concept ID
    normalizer_response = ncbi.search('NCBIgene:106')
    assertion_checks(normalizer_response, adcp1, 1, MatchType.CONCEPT_ID)

    # Symbol
    normalizer_response = ncbi.search('ADCP1')
    assertion_checks(normalizer_response, adcp1, 1, MatchType.SYMBOL)


def test_afa(ncbi, afa):
    """Test that AFA normalizes to correct gene concept."""
    # Concept ID
    normalizer_response = ncbi.search('NCBIgene:170')
    assertion_checks(normalizer_response, afa, 1, MatchType.CONCEPT_ID)

    # Symbol
    normalizer_response = ncbi.search('AFA')
    assertion_checks(normalizer_response, afa, 1, MatchType.SYMBOL)


def test_znf84(ncbi, znf84):
    """Test that ZNF84 normalizes to correct gene concept."""
    # Concept ID
    normalizer_response = ncbi.search('NCBIgene:7637')
    assertion_checks(normalizer_response, znf84, 1, MatchType.CONCEPT_ID)

    # Symbol
    normalizer_response = ncbi.search('ZNF84')
    assertion_checks(normalizer_response, znf84, 1, MatchType.SYMBOL)


def test_slc25a6(ncbi, slc25a6):
    """Test that SLC25A6 normalizes to correct gene concept."""
    # Concept ID
    normalizer_response = ncbi.search('NCBIgene:293')
    assertion_checks(normalizer_response, slc25a6, 1, MatchType.CONCEPT_ID)

    # Symbol
    normalizer_response = ncbi.search('SLC25A6')
    assertion_checks(normalizer_response, slc25a6, 1, MatchType.SYMBOL)


def test_loc106783576(ncbi, loc106783576):
    """Test that LOC106783576 normalizes to correct gene concept."""
    # Concept ID
    normalizer_response = ncbi.search('NCBIgene:106783576')
    assertion_checks(normalizer_response, loc106783576, 1,
                     MatchType.CONCEPT_ID)

    # Symbol
    normalizer_response = ncbi.search('LOC106783576')
    assertion_checks(normalizer_response, loc106783576, 1, MatchType.SYMBOL)


def test_oms(ncbi):
    """Test that OMS matches to correct gene concept."""
    normalizer_response = ncbi.search('NCBIgene:619538')
    assert normalizer_response['match_type'] == 0
    assert len(normalizer_response['records']) == 0


def test_glc1b(ncbi, glc1b):
    """Test that GLC1B normalizes to correct gene concept."""
    # Concept ID
    normalizer_response = ncbi.search('NCBIgene:2722')
    assertion_checks(normalizer_response, glc1b, 1, MatchType.CONCEPT_ID)

    # Symbol
    normalizer_response = ncbi.search('GLC1B')
    assertion_checks(normalizer_response, glc1b, 1, MatchType.SYMBOL)

    # associated_with
    normalizer_response = ncbi.search('omim:606689')
    assertion_checks(normalizer_response, glc1b, 1, MatchType.ASSOCIATED_WITH)


def test_hdpa(ncbi, hdpa):
    """Test that HDPA normalizes to correct gene concept."""
    # Concept ID
    normalizer_response = ncbi.search('NCBIgene:50829')
    assertion_checks(normalizer_response, hdpa, 1, MatchType.CONCEPT_ID)

    # Symbol
    normalizer_response = ncbi.search('HDPA')
    assertion_checks(normalizer_response, hdpa, 1, MatchType.SYMBOL)


def test_prkrap1(ncbi, prkrap1):
    """Test that PRKRAP1 normalizes to correct gene concept."""
    # Concept ID
    normalizer_response = ncbi.search('NCBIgene:731716')
    assertion_checks(normalizer_response, prkrap1, 1, MatchType.CONCEPT_ID)

    # Symbol
    normalizer_response = ncbi.search('PRKRAP1')
    assertion_checks(normalizer_response, prkrap1, 1, MatchType.SYMBOL)

    # xref
    normalizer_response = ncbi.search('hgnc:33447')
    assertion_checks(normalizer_response, prkrap1, 1, MatchType.XREF)


def test_mhb(ncbi, mhb):
    """Test that MHB normalizes to correct gene concept."""
    # Concept ID
    normalizer_response = ncbi.search('NCBIgene:619511')
    assertion_checks(normalizer_response, mhb, 1, MatchType.CONCEPT_ID)

    # Symbol
    normalizer_response = ncbi.search('MHB')
    assertion_checks(normalizer_response, mhb, 1, MatchType.SYMBOL)

    # associated_with
    normalizer_response = ncbi.search('OMIM:255160')
    assertion_checks(normalizer_response, mhb, 1, MatchType.ASSOCIATED_WITH)


def test_spg37(ncbi, spg37):
    """Test that SPG37 normalizes to correct gene concept."""
    # Concept ID
    normalizer_response = ncbi.search('NCBIgene:100049159')
    assertion_checks(normalizer_response, spg37, 1, MatchType.CONCEPT_ID)

    # Symbol
    normalizer_response = ncbi.search('SPG37')
    assertion_checks(normalizer_response, spg37, 1, MatchType.SYMBOL)

    # associated_with
    normalizer_response = ncbi.search('omim:611945')
    assertion_checks(normalizer_response, spg37, 1, MatchType.ASSOCIATED_WITH)


def test_discontinued_genes(ncbi):
    """Test searches for discontinued genes."""
    # HOTS
    normalizer_response = ncbi.search("ncbigene:103344718")
    check_ncbi_discontinued_gene(normalizer_response, 'ncbigene:103344718',
                                 'HOTS', 1, MatchType.CONCEPT_ID)

    normalizer_response = ncbi.search("HOTS")
    check_ncbi_discontinued_gene(normalizer_response, 'ncbigene:103344718',
                                 'HOTS', 1, MatchType.CONCEPT_ID)

    normalizer_response = ncbi.search("hots")
    check_ncbi_discontinued_gene(normalizer_response, 'ncbigene:103344718',
                                 'HOTS', 1, MatchType.CONCEPT_ID)

    # AASTH23
    normalizer_response = ncbi.search("ncbigene:544580")
    check_ncbi_discontinued_gene(normalizer_response, 'ncbigene:544580',
                                 'AASTH23', 1, MatchType.CONCEPT_ID)

    normalizer_response = ncbi.search("AASTH23")
    check_ncbi_discontinued_gene(normalizer_response, 'ncbigene:544580',
                                 'AASTH23', 1, MatchType.CONCEPT_ID)

    normalizer_response = ncbi.search("aastH23")
    check_ncbi_discontinued_gene(normalizer_response, 'ncbigene:544580',
                                 'AASTH23', 1, MatchType.CONCEPT_ID)


def test_no_match(ncbi):
    """Test that nonexistent query doesn't normalize to a match."""
    response = ncbi.search('cisplatin')
    assert response['match_type'] == 0
    assert len(response['records']) == 0
    # double-check that meta still populates
    assert response['source_meta_']['data_license'] == 'custom'
    assert response['source_meta_']['data_license_url'] == \
           'https://www.ncbi.nlm.nih.gov/home/about/policies/'
    assert datetime.strptime(response['source_meta_']['version'], "%Y%m%d")
    assert response['source_meta_']['data_url'] == \
        'ftp://ftp.ncbi.nlm.nih.gov'
    assert response['source_meta_']['rdp_url'] == \
        'https://reusabledata.org/ncbi-gene.html'
    assert not response['source_meta_']['data_license_attributes']['non_commercial']  # noqa: E501
    assert not response['source_meta_']['data_license_attributes']['share_alike']  # noqa: E501
    assert not response['source_meta_']['data_license_attributes']['attribution']  # noqa: E501

    # check blank
    response = ncbi.search('')
    assert response['match_type'] == 0

    # check some strange characters
    response = ncbi.search('----')
    assert response['match_type'] == 0

    response = ncbi.search('""')
    assert response['match_type'] == 0

    response = ncbi.search('~~~')
    assert response['match_type'] == 0

    response = ncbi.search(' ')
    assert response['match_type'] == 0

    # Incorrect Concept IDs
    response = ncbi.search('ncblgene:8193')
    assert response['match_type'] == 0

    response = ncbi.search('NCBIGENE54704')
    assert response['match_type'] == 0

    response = ncbi.search('54704')
    assert response['match_type'] == 0

    response = ncbi.search('ncbigene;54704')
    assert response['match_type'] == 0


def test_meta(ncbi, pdp1):
    """Test NCBI source metadata."""
    response = ncbi.search('PDP1')
    assert response['source_meta_']['data_license'] == 'custom'
    assert response['source_meta_']['data_license_url'] == \
        'https://www.ncbi.nlm.nih.gov/home/about/policies/'
    assert datetime.strptime(response['source_meta_']['version'], "%Y%m%d")
    assert response['source_meta_']['data_url'] == \
        'ftp://ftp.ncbi.nlm.nih.gov'
    assert response['source_meta_']['rdp_url'] == \
        'https://reusabledata.org/ncbi-gene.html'
    assert response['source_meta_']['genome_assemblies'] == ['GRCh38.p13']
    assert response['source_meta_']['data_license_attributes'] == {
        "non_commercial": False,
        "share_alike": False,
        "attribution": False
    }
