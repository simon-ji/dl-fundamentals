# Unit 5.5. Organizing Your Data Loaders with Data Modules

import lightning as L
import torch
from shared_utilities import LightningModel, MNISTDataModule, PyTorchMLP, AmesHousingDataModule
from watermark import watermark

if __name__ == "__main__":

    print(watermark(packages="torch,lightning", python=True))
    print("Torch CUDA available?", torch.cuda.is_available())

    torch.manual_seed(123)

    # dm = MNISTDataModule()
    dm = AmesHousingDataModule()

    pytorch_model = PyTorchMLP(num_features=3)

    lightning_model = LightningModel(model=pytorch_model, learning_rate=0.05)

    trainer = L.Trainer(
        max_epochs=10, accelerator="cpu", devices="auto", deterministic=True
    )
    trainer.fit(model=lightning_model, datamodule=dm)

    # train_acc = trainer.validate(dataloaders=dm.train_dataloader())[0]["val_acc"]
    # val_acc = trainer.validate(datamodule=dm)[0]["val_acc"]
    # test_acc = trainer.test(datamodule=dm)[0]["test_acc"]
    # print(
    #     f"Train Acc {train_acc*100:.2f}%"
    #     f" | Val Acc {val_acc*100:.2f}%"
    #     f" | Test Acc {test_acc*100:.2f}%"
    # )

    train_mse = trainer.validate(dataloaders=dm.train_dataloader())[0]["val_mse"]
    val_mse = trainer.validate(datamodule=dm)[0]["val_mse"]
    test_mse = trainer.test(datamodule=dm)[0]["test_mse"]
    print(
        f"Train MSE {train_mse:.2f}"
        f" | Val MSE {val_mse:.2f}"
        f" | Test MSE {test_mse*100:.2f}"
    )