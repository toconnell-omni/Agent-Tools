import os
import testutils.utils as utils
from agent_common.config import ConfigFactory
from agent_positouch.config import PositouchConfig
from agent_positouch.quick_menu.menu_data_importer import QuickMenuMenuDataImporter

# Call import process:

# QM_IMPORT_ZIP_SUBPATH = 'positouch_qm/QMxmlExportFiles.ZIP'
QM_IMPORT_ZIP_SUBPATH = 'positouch_qm/QMXmlExportFiles_2016.03.01_Discounts.zip'

config = ConfigFactory.config(PositouchConfig())

def test_qm_menu_import():
    
    # Setup:
    qmImporter = QuickMenuMenuDataImporter(config)
    import_zip_path = os.path.join(utils.TEST_DATA_PATH, QM_IMPORT_ZIP_SUBPATH)
    
    # Test:
    discounts, menu_items, menu_modifiers = qmImporter._import_from_zip(import_zip_path)
    
    # Results:
    print
    print('Results:')
    print
    print('    Discounts: ' + str(len(discounts.entries)))
    print('    Items:     ' + str(len(menu_items.entries)))
    print('    Modifiers: ' + str(len(menu_modifiers.entries)))


test_qm_menu_import()
