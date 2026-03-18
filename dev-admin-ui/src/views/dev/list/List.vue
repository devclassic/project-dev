<template>
  <el-breadcrumb separator="/" class="breadcrumb">
    <el-breadcrumb-item>起始页</el-breadcrumb-item>
    <el-breadcrumb-item>开发模板</el-breadcrumb-item>
    <el-breadcrumb-item>列表模板</el-breadcrumb-item>
  </el-breadcrumb>
  <div class="toolbar">
    <el-dropdown trigger="click">
      <el-button type="primary">功能操作</el-button>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item @click="showSearch">数据检索</el-dropdown-item>
          <el-dropdown-item @click="showCreate">添加数据</el-dropdown-item>
          <el-dropdown-item @click="batchDelete">批量删除</el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
  </div>
  <el-table
    :stripe="true"
    :border="true"
    :data="tableData"
    @selection-change="selectionChange"
    class="table">
    <el-table-column type="selection" width="38" />
    <el-table-column label="日期" min-width="200">
      <template #default="scope">{{ scope.row.date }}</template>
    </el-table-column>
    <el-table-column label="姓名" prop="name" min-width="200" />
    <el-table-column label="超出悬浮" prop="address" min-width="200" show-overflow-tooltip />
    <el-table-column label="地址" prop="address" min-width="400" />
    <el-table-column label="操作" fixed="right" min-width="200">
      <template #default="scope">
        <el-button type="primary" size="small" @click="showInfo(scope.row)">查看</el-button>
        <el-button type="success" size="small" @click="edit(scope.row)">编辑</el-button>
        <el-popconfirm title="是否确认删除？" @confirm="remove(scope.row)">
          <template #reference>
            <el-button type="danger" size="small">删除</el-button>
          </template>
        </el-popconfirm>
      </template>
    </el-table-column>
  </el-table>
  <div class="pager">
    <el-pagination
      :total="400"
      background
      size="small"
      layout="total, sizes, prev, pager, next, jumper"
      @change="pageChange" />
  </div>

  <el-dialog v-model="state.showSearch" title="数据检索" width="600">
    <el-form label-width="auto">
      <el-form-item label="姓名" class="form-item">
        <el-input />
      </el-form-item>
      <el-form-item label="年龄" class="form-item">
        <el-input />
      </el-form-item>
      <el-form-item label="所在班级" class="form-item">
        <el-input />
      </el-form-item>
    </el-form>
    <template #footer>
      <el-button @click="state.showSearch = false">取消</el-button>
      <el-button type="primary" @click="state.showSearch = false">确认</el-button>
    </template>
  </el-dialog>

  <el-dialog v-model="state.showEdit" :title="`${editType}数据`" width="600">
    <el-form label-width="auto">
      <el-form-item label="姓名" class="form-item">
        <el-input />
      </el-form-item>
      <el-form-item label="年龄" class="form-item">
        <el-input />
      </el-form-item>
      <el-form-item label="所在班级" class="form-item">
        <el-input />
      </el-form-item>
    </el-form>
    <template #footer>
      <el-button @click="state.showEdit = false">取消</el-button>
      <el-button type="primary" @click="state.showEdit = false">确认</el-button>
    </template>
  </el-dialog>

  <el-dialog v-model="state.showInfo" title="数据详细" width="600">
    <table class="info-table">
      <tbody>
        <tr>
          <td>姓名：</td>
          <td>测试数据</td>
        </tr>
        <tr>
          <td>年龄：</td>
          <td>测试数据</td>
        </tr>
        <tr>
          <td>所在班级：</td>
          <td>测试数据</td>
        </tr>
      </tbody>
    </table>
    <template #footer>
      <el-button @click="state.showInfo = false">取消</el-button>
      <el-button type="primary" @click="state.showInfo = false">确认</el-button>
    </template>
  </el-dialog>
</template>

<script setup>
  import { reactive, computed } from 'vue'
  import { ElMessage, ElMessageBox } from 'element-plus'

  const tableData = [
    {
      date: '2016-05-04',
      name: 'Aleyna Kutzner',
      address: 'Lohrbergstr. 86c, Süd Lilli, Saarland',
    },
    {
      date: '2016-05-03',
      name: 'Helen Jacobi',
      address: '760 A Street, South Frankfield, Illinois',
    },
    {
      date: '2016-05-02',
      name: 'Brandon Deckert',
      address: 'Arnold-Ohletz-Str. 41a, Alt Malinascheid, Thüringen',
    },
    {
      date: '2016-05-01',
      name: 'Margie Smith',
      address: '23618 Windsor Drive, West Ricardoview, Idaho',
    },
  ]

  const state = reactive({
    selectedRows: [],
    editType: '',
    data: {},
    showSearch: false,
    showEdit: false,
    showInfo: false,
  })

  const editType = computed(() => {
    let type = ''
    switch (state.editType) {
      case 'create':
        type = '添加'
        break
      case 'edit':
        type = '编辑'
        break
    }
    return type
  })

  const selectionChange = val => {
    state.selectedRows = val
  }

  const showSearch = () => {
    state.showSearch = true
  }

  const showCreate = () => {
    state.editType = 'create'
    state.data = {}
    state.showEdit = true
  }

  const showInfo = row => {
    state.data = row
    state.showInfo = true
  }

  const batchDelete = async () => {
    if (state.selectedRows.length === 0) {
      ElMessage.warning('请选择要批量删除的数据')
      return
    }
    await ElMessageBox.confirm('确认删除选中的数据吗？', '提示', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    })
    ElMessage.success('删除成功')
  }

  const edit = row => {
    state.editType = 'edit'
    state.data = row
    state.showEdit = true
  }

  const remove = row => {
    console.log(row)
  }

  const pageChange = (page, size) => {
    console.log(page, size)
  }
</script>

<style scoped lang="scss"></style>
