# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from jax.interpreters.sharded_jit import (
  sharded_jit as sharded_jit,
  with_sharding_constraint as with_sharding_constraint,
)
from jax.interpreters.pxla import PartitionSpec as PartitionSpec
from jax.experimental.x64_context import (
  enable_x64 as enable_x64,
  disable_x64 as disable_x64,
)
