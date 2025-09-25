import os
import shutil
import sys

def main():
    if len(sys.argv) != 3:
        print("用法: python create_project.py <项目名称> <语言类型>")
        print("语言类型支持: go, frontend, python, C, C++")
        return

    project_name = sys.argv[1]
    language = sys.argv[2].lower()
    valid_languages = ["go", "frontend", "python", "C", "C++"]

    if language not in valid_languages:
        print(f"❌ 不支持的语言类型: {language}")
        return

    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    new_project_path = os.path.join(parent_dir, project_name)

    # 重命名当前目录为项目名称
    os.rename(current_dir, new_project_path)
    os.chdir(new_project_path)

    # 复制模板文件
    rel_language = "cpp" if language in ["C", "C++"] else language
    template_dir = os.path.join(new_project_path, rel_language)
    workspace_filename = f"{rel_language}.code-workspace"
    src = os.path.join(template_dir, workspace_filename)
    dst = os.path.join(new_project_path, workspace_filename.replace(rel_language + "-template", project_name))
    shutil.copyfile(src, dst)
    print(f"✅ 已复制: {dst}")

    # 复制gitignore
    gitignore_filename = f"{language}.gitignore" if language in ["C", "C++"] else ".gitignore"
    src = os.path.join(template_dir, gitignore_filename)
    dst = os.path.join(new_project_path, ".gitignore")
    shutil.copyfile(src, dst)
    print(f"✅ 已复制: {dst}")

    # 删除模板目录
    for lang in valid_languages:
        lang_dir = os.path.join(new_project_path, lang)
        if os.path.isdir(lang_dir):
            shutil.rmtree(lang_dir)
            print(f"🧹 已删除模板目录: {lang_dir}")

    print(f"\n🎉 项目初始化完成！路径: {new_project_path}")

if __name__ == "__main__":
    main()
