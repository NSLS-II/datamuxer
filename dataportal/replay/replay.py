
import enaml
from enaml.qt.qt_application import QtApplication
import numpy as np

from dataportal.muxer.api import DataMuxer
from dataportal.replay.search import (GetLastModel, WatchForHeadersModel,
                                      DisplayHeaderModel)
from dataportal.replay.muxer import MuxerModel
from dataportal.replay.scalar import ScalarCollection
import sys

import metadatastore

#metadatastore.conf.mds_config['host'] = 'localhost'
#metadatastore.conf.mds_config['database'] = 'test'

with enaml.imports():
    from dataportal.replay.replay_view import MainView

def define_default_params():
    params_dict = {
        'search_tab_index': 0,
        'automatically_update_header': False,
    }
    return params_dict

def define_ophyd_params():
    params_dict = {
        'search_tab_index': 1,
        'automatically_update_header': True,
    }
    return params_dict

def create_default_ui(init_params_dict):
    get_last_model = GetLastModel()
    muxer_model = MuxerModel()
    scalar_collection = ScalarCollection()
    display_header_model = DisplayHeaderModel()
    watch_headers_model = WatchForHeadersModel()
    watch_headers_model.auto_update = init_params_dict['automatically_update_header']


    # set up observers
    muxer_model.observe('data_muxer', scalar_collection.new_data_muxer)
    muxer_model.new_data_callbacks.append(scalar_collection.notify_new_data)

    watch_headers_model.observe('header', display_header_model.new_run_header)
    get_last_model.observe('header', display_header_model.new_run_header)
    display_header_model.observe('header', muxer_model.new_run_header)


    get_last_model.observe('selected', scalar_collection.header_changed)

    main_view = MainView(get_last_model=get_last_model, muxer_model=muxer_model,
                         scalar_collection=scalar_collection,
                         watch_headers_model=watch_headers_model,
                         display_header_model=display_header_model,
                         init_params=init_params_dict)
    return main_view

def main():
    args = sys.argv
    params_dict = define_default_params()
    if '--ophyd' in args:
        params_dict = define_ophyd_params()
    app = QtApplication()
    ui = create_default_ui(params_dict)
    ui.show()
    app.start()

if __name__ == "__main__":
    main()
