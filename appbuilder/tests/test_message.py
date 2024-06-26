# Copyright (c) 2023 Baidu, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import unittest
from appbuilder.core.message import Message


@unittest.skipUnless(os.getenv("TEST_CASE", "UNKNOWN") == "CPU_PARALLEL", "")
class TestMessage(unittest.TestCase):
    def setUp(self):
        """
        pass
        """
        pass

    def test_message(self):
        """
        test message
        """
        m = Message({"query": "my message"}, name="m")
        print(m)
        m = Message(content={"query": "my message"}, name="m")
        print(m)

if __name__ == "__main__":
    unittest.main()
