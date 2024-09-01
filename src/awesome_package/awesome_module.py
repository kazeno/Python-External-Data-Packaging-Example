# awesome_module.py:

import importlib.util
import os
import shutil
import sysconfig


def copy_auxiliary_data_into_current_dir():
    """
    Copy all the auxiliary data files from the system data directory into the current directory.

    The auxiliary data files were installed into the system data directory during the wheel package installation.
    This function shows how you can access them afterwards from any module in the package.

    Returns
    -------
    None
    """
    data_dir = sysconfig.get_path('data')
    result = False

    try:
        shutil.copytree(
            os.path.join(
                data_dir,
                'awesome_auxiliary_data'
            ),
            '.',
            dirs_exist_ok=True
        )
        result = True
    except FileNotFoundError:
        print(
            f"The awesome_auxiliary_data directory was not found in {data_dir}. Try uninstalling and reinstalling this library"
        )
    except shutil.Error as e:
        print(f"Error occurred while copying: {e}")

    if result:
        print("Copied all auxiliary data files into the current directory!")


def run_auxiliary_scripts():
    """
    Import and run the auxiliary scripts from the system scripts directory.

    The auxiliary scripts were installed into the system scripts directory during the wheel package installation.
    This function shows how you can import and use them afterwards from any module in the package.

    Returns
    -------
    None
    """
    scripts_dir = sysconfig.get_path('scripts')

    decrease_world_suck_path = os.path.join(
        scripts_dir,
        'awesome_auxiliary_scripts',
        'decrease_world_suck.py'
    )
    generate_awesomeness_path = os.path.join(
        scripts_dir,
        'awesome_auxiliary_scripts',
        'generate_awesomeness.py'
    )

    if (
        not os.path.isfile(decrease_world_suck_path)
        or not os.path.isfile(generate_awesomeness_path)
    ):
        print(
            f"The auxiliary scripts were not found in {scripts_dir}. Try uninstalling and reinstalling this library"
        )
    else:
        decrease_world_suck_module = _import_module(
            'decrease_world_suck',
            decrease_world_suck_path
        )
        decrease_world_suck_module.decrease_world_suck()

        generate_awesomeness_module = _import_module(
            'generate_awesomeness',
            generate_awesomeness_path
        )
        generate_awesomeness_module.generate_awesomeness()


def _import_module(module_name, module_path):
    """
    Import module `module_name` from path `module_path`.

    This allows you to import a module from any arbitrary path in the system.

    Parameters
    ----------
    module_name: str
        The name of the module to import.

    module_path: str
        The path to the module file.

    Returns
    -------
    module: module
        The imported module.

    """
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


if __name__ == "__main__":
    copy_auxiliary_data_into_current_dir()
    run_auxiliary_scripts()
