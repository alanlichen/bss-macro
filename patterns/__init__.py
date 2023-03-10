#  Stumpy Macro - Easy to use macro for Bee Swarm Simulator
#  Copyright (C) 2023 Alan Chen
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import importlib

cached_patterns = {}


def farm_pattern(pattern_name):
    if pattern_name not in cached_patterns:
        pattern = importlib.import_module(f"patterns.{pattern_name}")
        cached_patterns[pattern_name] = pattern
    else:
        pattern = cached_patterns[pattern_name]
    pattern.execute()
