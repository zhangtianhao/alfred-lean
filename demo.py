#!/usr/bin/python
# encoding: utf-8

import sys
import logging

from workflow import Workflow3

log = logging


def main(wf):
    args = wf.args

    log.debug(args[0])

    # 组装 alfred 列表展示数据
    wf.add_item(title='条目标题', subtitle='条目说明',arg='条目参数,回车后这里会作为参数往下游传递', valid=True)

    # 让 alfred 显示列表数据
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()

    log = wf.logger

    sys.exit(wf.run(main))
