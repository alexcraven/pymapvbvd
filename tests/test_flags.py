"""
Created by shahdloo
22/09/2020
"""

import os.path as op
import numpy as np
from core import mapVBVD

test_data_vb_broken = op.join(op.dirname(__file__), 'test_data', 'meas_MID111_sLaser_broken_FID4873.dat')
test_data_gre = op.join(op.dirname(__file__), 'test_data', 'meas_MID00255_FID12798_GRE_surf.dat')
test_data_epi = op.join(op.dirname(__file__), 'test_data', 'meas_MID00265_FID12808_FMRI.dat')


def test_flagRemoveOS():
    twixObj = mapVBVD(test_data_gre, quiet=False)
    twixObj[1].image.flagRemoveOS = False
    assert np.allclose(twixObj[1].image.dataSize, [256, 15, 128, 96, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    twixObj[1].image.flagRemoveOS = True
    assert np.allclose(twixObj[1].image.dataSize, [128, 15, 128, 96, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

    # broken file
    twixObj = mapVBVD(test_data_vb_broken, quiet=False)
    twixObj.image.flagRemoveOS = False
    assert np.allclose(twixObj.image.dataSize, [4096, 32, 1, 1, 1, 1, 1, 1, 1, 97, 1, 1, 1, 1, 1, 1])
    twixObj.image.flagRemoveOS = True
    assert np.allclose(twixObj.image.dataSize, [2048, 32, 1, 1, 1, 1, 1, 1, 1, 97, 1, 1, 1, 1, 1, 1])


def test_flagIgnoreSeg_flagDoAverage():
    twixObj = mapVBVD(test_data_epi, quiet=False)

    twixObj[1].refscanPC.flagIgnoreSeg = False
    twixObj[1].refscanPC.flagDoAverage = False
    assert np.allclose(twixObj[1].refscanPC.dataSize, [86, 15, 1, 1, 36, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1])
    twixObj[1].refscanPC.flagDoAverage = True
    assert np.allclose(twixObj[1].refscanPC.dataSize, [86, 15, 1, 1, 36, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1])

    twixObj[1].refscanPC.flagIgnoreSeg = True
    twixObj[1].refscanPC.flagDoAverage = False
    assert np.allclose(twixObj[1].refscanPC.dataSize, [86, 15, 1, 1, 36, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    twixObj[1].refscanPC.flagDoAverage = True
    assert np.allclose(twixObj[1].refscanPC.dataSize, [86, 15, 1, 1, 36, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])


def test_flagSkipToFirstLine():
    twixObj = mapVBVD(test_data_epi, quiet=False)

    twixObj[1].refscan.flagSkipToFirstLine = False
    assert np.allclose(twixObj[1].refscan.dataSize, [86, 15, 55, 1, 36, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1])
    twixObj[1].refscan.flagSkipToFirstLine = True
    assert np.allclose(twixObj[1].refscan.dataSize, [86, 15, 24, 1, 36, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1])
